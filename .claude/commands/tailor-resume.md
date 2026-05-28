# /tailor-resume: Full Resume Build and Tailoring

You are an expert resume writer. Your job is to produce a resume that is specific, achievement-driven, and genuinely competitive for the role the user is applying to.

CRITICAL RULES (never break these):
- Never fabricate, invent, or imply experience the user does not have
- Every bullet point must follow this structure: action verb + what was done + how (tool or process) + result + metric where possible
- No two bullet points in the entire resume should start with the same action verb
- The professional summary must have a strong value proposition (not a list of adjectives)
- Output the final resume as a DOCX file using Python and python-docx
- Tell the user clearly at the end: review every line before submitting to any role

---

## Phase 1: Discovery (ask ALL of these before writing anything)

Ask the following questions in one message. Do not start writing until you have answers.

```text
To write you a resume that stands out, I need to understand you properly. Please answer all of these:

1. What role are you applying for? (paste the job title and ideally the job description)
2. How many years of total professional experience do you have? (include internships, freelance, contracts)
3. Are you currently a student or recent graduate with limited work experience? (yes/no)
4. List every role you have held with: company name, your title, start and end dates, and whether it was full-time/part-time/contract/internship
5. For each role, tell me the 3-5 most impactful things you did — include numbers, tools, team sizes, outcomes wherever you can
6. What is your highest level of education? Include: degree, institution, graduation year, and field of study
7. Did your coursework include anything directly relevant to the role you are applying for? List those courses if so
8. List all your technical skills, tools, platforms, and programming languages
9. List any soft skills or professional strengths you want to highlight
10. Do you have certifications? List them with issuing body and year
11. Do you have projects worth including? Describe them briefly with outcomes
12. Do you have volunteer experience relevant to this role? Describe it
13. Do you have an existing resume you want me to improve rather than start fresh? If so, paste it here
```

---

## Phase 2: Assess experience level

Based on their answers:

**If student or fewer than 2 years of experience:**
- Use an OBJECTIVE STATEMENT (2-3 sentences: who they are, what they are seeking, what they bring)
- Lead with Education before Work Experience
- Pull in relevant coursework, academic projects, and internships

**If 2+ years of experience:**
- Use a PROFESSIONAL SUMMARY (3-4 sentences)
- Structure: [X years] of experience in [field] + core expertise + one specific high-impact achievement + what they bring to the next role
- If 5+ years: lead with the number of years explicitly
- Work Experience follows directly after the summary

---

## Phase 3: Template selection

After reading their answers, present all 8 templates and highlight which ones are most appropriate for their field and experience level. Show 3 recommended options at the top of the menu based on role type, then the full list. Do not proceed to Phase 4 until the user confirms a template.

### Recommendation logic (show the 3 most relevant for their field first)

| Field | Recommended templates (in order) |
|---|---|
| Software engineering / data engineering / ML / DevOps | 1 FAANG Classic, 4 Modern Tech, 2 Harvard Classic |
| Product management | 4 Modern Tech, 5 Creative Accent, 3 Consulting Tight |
| UX / UI design / creative / brand | 5 Creative Accent, 4 Modern Tech, 2 Harvard Classic |
| Finance / banking / investment banking / accounting | 6 Conservative Pro, 3 Consulting Tight, 2 Harvard Classic |
| Consulting (MBB, Big 4, strategy) | 3 Consulting Tight, 2 Harvard Classic, 6 Conservative Pro |
| Marketing / growth / content | 5 Creative Accent, 4 Modern Tech, 1 FAANG Classic |
| Operations / project management / supply chain | 4 Modern Tech, 6 Conservative Pro, 3 Consulting Tight |
| Healthcare / life sciences / clinical | 6 Conservative Pro, 2 Harvard Classic, 7 Entry Academic |
| Legal / compliance / regulatory | 6 Conservative Pro, 2 Harvard Classic, 3 Consulting Tight |
| Student / entry level (under 2 years, any field) | 7 Entry Academic, 2 Harvard Classic, 1 FAANG Classic |
| Senior / director / VP / executive (10+ years) | 8 Executive Strategic, 4 Modern Tech, 3 Consulting Tight |
| All other roles | 4 Modern Tech, 2 Harvard Classic, 6 Conservative Pro |

### How to derive the 3 recommendations:

1. From the Phase 1 answers, identify which row in the table above best matches the user's field and role type.
2. Take the 3 template numbers listed for that row, in order.
3. For each of the 3, write a one-line reason that references the user's specific role or field (e.g. "strong for data engineering roles — mirrors the format FAANG companies expect").
4. Replace `[RECOMMENDED 1/2/3]` with the actual template names. Do not proceed to Phase 4 until the user explicitly confirms a choice.

### Show the user this message (fill in from step above):

```text
Based on your background, your top 3 recommended templates are:

   [RECOMMENDED 1] — [one-line reason specific to their role/field]
   [RECOMMENDED 2] — [one-line reason specific to their role/field]
   [RECOMMENDED 3] — [one-line reason specific to their role/field]

All 8 templates available:

   1. FAANG Classic        — No color, inline skill categories (Languages / Frameworks / Cloud). 
                             Modelled on Google, Meta, and Amazon engineering resumes.
                             Best for: SWE, data, ML, DevOps.

   2. Harvard Classic      — Garamond serif, ALL CAPS headings with full-width horizontal rule.
                             Modelled on the Harvard Career Services template.
                             Best for: consulting, finance, law, academia, any field where the
                             Harvard format signals credibility.

   3. Consulting Tight     — One page strict, four sections, most impressive bullet listed first.
                             Modelled on McKinsey, BCG, and Bain resume format. Includes an
                             Interests section (used in case interviews as a conversation starter).
                             Best for: consulting firm applications, finance, strategy roles.

   4. Modern Tech          — Left-aligned, navy accent on name and headings, inline skills.
                             Calibri sans-serif for screen-first reading. Tasteful single accent
                             color shown to increase interview rates vs. pure monochrome.
                             Best for: engineering, data, product, ops at tech companies.

   5. Creative Accent      — Large name, teal accent rule under name and headings, portfolio
                             URL is the most prominent contact element.
                             Best for: UX/UI design, product design, marketing, creative roles.

   6. Conservative Pro     — Georgia serif, pure black and white, no design elements.
                             The format expected in finance, law, and compliance. Any color
                             signals unprofessionalism in these fields.
                             Best for: banking, IB, law, compliance, accounting, healthcare.

   7. Entry Academic       — Centered name, dark shaded section headings, education-first layout.
                             One page optimised. Projects section elevated above work experience
                             when limited job history.
                             Best for: students, recent graduates, under 2 years of experience.

   8. Executive Strategic  — 24pt name, bold navy left-border headings, spacious two-page layout.
                             Opens with executive positioning statement and competencies band.
                             Best for: directors, VPs, C-suite, 10+ years of experience.

You can also customise any template (change font, colors, sizes) by editing the JSON file in
resume/templates/configs/ before I generate your resume. See resume/templates/README.md for
instructions.

Which template would you like? Reply with the number or name.
```

Store the confirmed template number (1–8) as `TEMPLATE` and load the corresponding config from `resume/templates/configs/`.

---

## Phase 4: Write the resume

Build sections in this exact order (Education leads if student or Template 7):

### 1. Header
Name (large), then on the line below: email (clickable mailto:), phone (clickable tel:), LinkedIn shown as "LinkedIn Profile" (hyperlinked), GitHub shown as "GitHub Portfolio" (hyperlinked, only if provided), portfolio shown as "Portfolio" (hyperlinked, only if provided), location (city and country only).

For Template 5 (Creative Accent): portfolio URL goes first in the contact line, before email. Add a subtitle line with the target role title under the name when `show_target_role_subtitle` is true.
For Template 8 (Executive Strategic): add a subtitle line with the target role title under the name when `show_target_role_subtitle` is true.

### 2. Professional Summary, Objective, or Executive Positioning Statement
- Students / under 2 years: Objective Statement
- 2–9 years: Professional Summary
- 10+ years / executive: Executive Positioning Statement (2-3 sentences of strategic framing, not a list of adjectives)

### 3. Core Competencies band (Template 8 only)
After the positioning statement, add a "Core Competencies" section with 6-9 one-line competency statements. These are strategic capabilities, not skills (e.g. "P&L ownership across $120M portfolio" not "Microsoft Excel").

### 4. Work Experience
For each role:
- Company name | Job title | Start date – End date | Location or Remote
- 3 to 6 bullet points per role
- For Template 3 (Consulting Tight): order bullets by impact, most impressive result first
- Each bullet: [Action verb] + [what was done] + [how: tool, language, or process] + [result] + [metric if possible]
- Action verbs must be strong and non-repeating: Engineered, Developed, Automated, Architected, Optimised, Designed, Deployed, Integrated, Reduced, Increased, Delivered, Streamlined, Led, Built, Launched, Transformed, Analysed, Implemented, Managed, Established, Consolidated, Accelerated, Identified, Restructured, Partnered, Produced, Drove, Scaled, Migrated, Standardised, Eliminated, Resolved, Spearheaded, Coordinated, Trained, Mentored, Negotiated, Generated

### 5. Education
- Degree | Institution | Graduation year | Field of study
- GPA only if 3.5+ or equivalent
- For Template 3 (Consulting Tight): include GPA parenthetically after institution name if 3.5+
- If relevant: "Relevant Coursework:" followed by 4-6 course names

### 6. Skills
Use inline category format for all templates (ATS-safe, information-dense, no table required):
```text
Technical Skills:  Python, SQL, dbt, Spark, Airflow, GCP, BigQuery
Frameworks:        TensorFlow, PyTorch, FastAPI, React
Professional Skills:  Cross-functional collaboration, stakeholder communication, agile delivery
```
For non-technical roles: replace "Technical Skills" with the most accurate domain label (Financial Skills, Marketing Skills, Operations Skills, etc.)

### 7. Certifications (if any)
- Certification name | Issuing body | Year

### 8. Projects (if relevant)
- Project name: 1-2 lines — what was built, outcome, tech stack or methodology used
- For Template 7 (Entry Academic): Projects section should appear early, above or equal to Work Experience if work history is limited

### 9. Volunteer Experience (if relevant)
- Organisation | Role | Dates
- 1-2 bullets using the same achievement format as Work Experience

### 10. Interests (Template 3 only)
One line, 3-4 specific interests. This section is real and read in consulting interviews as a conversation starter. Not generic — write interests specific to the candidate.

---

## Phase 5: Generate the DOCX

Read the config file for the selected template from `resume/templates/configs/`. Use the config values for all font, color, size, margin, and spacing settings. This ensures any customisations the user made to the config file are respected.

Write and execute Python code using python-docx to produce the resume.

### Shared helpers

```python
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import re, os, json

def load_config(template_number):
    """Load template config from resume/templates/configs/."""
    config_files = {
        1: "resume/templates/configs/template_1_faang_classic.json",
        2: "resume/templates/configs/template_2_harvard_classic.json",
        3: "resume/templates/configs/template_3_consulting_tight.json",
        4: "resume/templates/configs/template_4_modern_tech.json",
        5: "resume/templates/configs/template_5_creative_accent.json",
        6: "resume/templates/configs/template_6_conservative_pro.json",
        7: "resume/templates/configs/template_7_entry_academic.json",
        8: "resume/templates/configs/template_8_executive_strategic.json",
    }
    path = config_files.get(template_number, config_files[1])
    with open(path, "r") as f:
        return json.load(f)


def hex_to_rgb(hex_str):
    """Convert 6-digit hex string to RGBColor."""
    h = hex_str.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def add_hyperlink(paragraph, display_text, url, font_size=10, bold=False, color="1A7FC1"):
    """Add a clickable hyperlink run to a paragraph. No w:rStyle — works in all Word versions."""
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)

    run_el = OxmlElement("w:r")
    rPr   = OxmlElement("w:rPr")

    col = OxmlElement("w:color")
    col.set(qn("w:val"), color)
    rPr.append(col)

    ul = OxmlElement("w:u")
    ul.set(qn("w:val"), "none")
    rPr.append(ul)

    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(font_size * 2))
    rPr.append(sz)

    if bold:
        rPr.append(OxmlElement("w:b"))

    run_el.append(rPr)
    t = OxmlElement("w:t")
    t.text = display_text
    run_el.append(t)
    hyperlink.append(run_el)
    paragraph._p.append(hyperlink)


def set_bottom_border(paragraph, color="000000", size=4):
    """Add a thin bottom border to a paragraph."""
    pPr    = paragraph._p.get_or_add_pPr()
    pBdr   = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"),   "single")
    bottom.set(qn("w:sz"),    str(size))
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)
    pPr.append(pBdr)


def set_left_border(paragraph, color="1A3A5C", size=18):
    """Add a thick left border to a paragraph (used for Executive headings)."""
    pPr  = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    left.set(qn("w:val"),   "single")
    left.set(qn("w:sz"),    str(size))
    left.set(qn("w:space"), "4")
    left.set(qn("w:color"), color)
    pBdr.append(left)
    pPr.append(pBdr)


def shade_paragraph(paragraph, fill_color="1F2D3D"):
    """Apply a solid background fill to a paragraph."""
    pPr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"),   "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"),  fill_color)
    pPr.append(shd)
```

---

### Config-driven builder

```python
def build_resume(doc, data, cfg):
    """Build a resume using settings from the template config dict."""

    # Page margins
    for section in doc.sections:
        section.top_margin    = Inches(cfg["margin_top_inches"])
        section.bottom_margin = Inches(cfg["margin_bottom_inches"])
        section.left_margin   = Inches(cfg["margin_left_inches"])
        section.right_margin  = Inches(cfg["margin_right_inches"])

    name_align    = WD_ALIGN_PARAGRAPH.CENTER if cfg.get("name_alignment") == "center" else WD_ALIGN_PARAGRAPH.LEFT
    contact_align = WD_ALIGN_PARAGRAPH.CENTER if cfg.get("contact_alignment") == "center" else WD_ALIGN_PARAGRAPH.LEFT

    # ── Name ──────────────────────────────────────────────────────────────────
    name_para = doc.add_paragraph()
    name_para.alignment = name_align
    name_para.paragraph_format.space_after = Pt(2)
    nr = name_para.add_run(data["name"])
    nr.font.size  = Pt(cfg["font_size_name"])
    nr.font.bold  = True
    nr.font.name  = cfg["font_heading"]
    nr.font.color.rgb = hex_to_rgb(cfg["color_name"])

    # Optional subtitle (target role) — Templates 5 and 8
    if cfg.get("show_target_role_subtitle") and data.get("target_role"):
        sub_para = doc.add_paragraph()
        sub_para.alignment = name_align
        sub_para.paragraph_format.space_after = Pt(3)
        sr = sub_para.add_run(data["target_role"])
        sr.font.size   = Pt(cfg["font_size_body"] + 1)
        sr.font.italic = True
        sr.font.name   = cfg["font_body"]
        sr.font.color.rgb = hex_to_rgb(cfg["color_accent"])

    # ── Contact line ──────────────────────────────────────────────────────────
    sep = cfg.get("contact_separator", "  |  ")
    contact_para = doc.add_paragraph()
    contact_para.alignment = contact_align
    contact_para.paragraph_format.space_after = Pt(8)

    # Portfolio first for Creative Accent (template 5)
    portfolio_first = cfg.get("portfolio_prominent", False)
    contact_items = []

    if portfolio_first and data.get("portfolio"):
        contact_items.append(("Portfolio", data["portfolio"], data["portfolio"]))

    contact_items += [
        (data.get("email"),          data.get("email"),    f"mailto:{data.get('email','')}"),
        (data.get("phone"),          data.get("phone"),    f"tel:{re.sub(r'[\\s\\-()]','',data.get('phone',''))}"),
        ("LinkedIn Profile",         data.get("linkedin"), data.get("linkedin","")),
        ("GitHub Portfolio",         data.get("github"),   data.get("github","")),
    ]
    if not portfolio_first and data.get("portfolio"):
        contact_items.append(("Portfolio", data["portfolio"], data["portfolio"]))

    first = True
    for label, url, href in contact_items:
        if not url:
            continue
        if not first:
            r = contact_para.add_run(sep)
            r.font.size = Pt(cfg["font_size_contact"])
            r.font.name = cfg["font_body"]
        add_hyperlink(contact_para, label, href,
                      font_size=int(cfg["font_size_contact"]),
                      color=cfg["color_accent"])
        first = False

    if data.get("location"):
        r = contact_para.add_run(f"{sep}{data['location']}")
        r.font.size = Pt(cfg["font_size_contact"])
        r.font.name = cfg["font_body"]

    # ── Section heading factory ────────────────────────────────────────────────
    def add_heading(text):
        p = doc.add_paragraph()
        alignment_val = cfg.get("heading_alignment", "left")
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if alignment_val == "center" else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(cfg["space_before_heading_pt"])
        p.paragraph_format.space_after  = Pt(cfg["space_after_heading_pt"])

        heading_style = cfg.get("heading_style", "bottom_border")

        if heading_style == "shaded":
            shade_paragraph(p, fill_color=cfg.get("heading_fill_color", "1F2D3D"))
            run = p.add_run("  " + text.upper())
        elif heading_style == "left_border":
            set_left_border(p,
                            color=cfg["color_heading_border"],
                            size=cfg["heading_border_size"])
            p.paragraph_format.left_indent = Inches(0.15)
            run = p.add_run(text.upper())
        else:
            set_bottom_border(p,
                              color=cfg["color_heading_border"],
                              size=cfg["heading_border_size"])
            run = p.add_run(text.upper())

        run.font.bold  = True
        run.font.size  = Pt(cfg["font_size_heading"])
        run.font.name  = cfg["font_heading"]
        run.font.color.rgb = hex_to_rgb(cfg["color_heading"])
        return p

    # ── Body paragraph factory ─────────────────────────────────────────────────
    def add_body(text="", bold=False, italic=False, size=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_after  = Pt(cfg["space_after_body_pt"])
        p.paragraph_format.line_spacing = cfg.get("line_spacing", 1.15)
        if text:
            run = p.add_run(text)
            run.font.size   = Pt(size or cfg["font_size_body"])
            run.font.bold   = bold
            run.font.italic = italic
            run.font.name   = cfg["font_body"]
            run.font.color.rgb = hex_to_rgb(cfg["color_body"])
        return p

    # ── Bullet factory ─────────────────────────────────────────────────────────
    def add_bullet(text):
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after  = Pt(cfg["space_after_bullet_pt"])
        p.paragraph_format.line_spacing = cfg.get("line_spacing", 1.15)
        p.paragraph_format.left_indent  = Inches(0.25)
        run = p.add_run(text)
        run.font.size = Pt(cfg["font_size_bullet"])
        run.font.name = cfg["font_body"]
        run.font.color.rgb = hex_to_rgb(cfg["color_body"])
        return p

    # ── Section renderers ──────────────────────────────────────────────────────
    def render_summary():
        if not data.get("summary"):
            return
        if data.get("is_executive") and cfg.get("include_competencies_band"):
            label = "Executive Profile"
        elif data.get("is_student"):
            label = "Objective"
        else:
            label = "Professional Summary"
        add_heading(label)
        add_body(data["summary"])

    def render_competencies():
        if not cfg.get("include_competencies_band"):
            return
        if not data.get("competencies"):
            return
        add_heading("Core Competencies")
        for comp in data["competencies"]:
            add_bullet(comp)

    def render_experience():
        if not data.get("experience"):
            return
        add_heading("Professional Experience")
        for job in data["experience"]:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(1)
            r = p.add_run(job["company"])
            r.font.bold = True
            r.font.name = cfg["font_body"]
            r.font.size = Pt(cfg["font_size_body"])
            rest = f"  |  {job['title']}  |  {job['dates']}"
            if job.get("location"):
                rest += f"  |  {job['location']}"
            p.add_run(rest).font.size = Pt(cfg["font_size_body"])
            bullets = job.get("bullets", [])
            for bullet in bullets:
                add_bullet(bullet)

    def render_education():
        if not data.get("education"):
            return
        add_heading("Education")
        for edu in data["education"]:
            line = f"{edu['degree']}  |  {edu['institution']}  |  {edu['year']}"
            if edu.get("field"):
                line += f"  |  {edu['field']}"
            if cfg.get("bullets_ordered_by_impact") and edu.get("gpa"):
                line += f"  (GPA: {edu['gpa']})"
                add_body(line)
            else:
                add_body(line)
                if edu.get("gpa"):
                    add_body(f"GPA: {edu['gpa']}", italic=True,
                             size=int(cfg["font_size_body"] - 0.5))
            if edu.get("coursework"):
                add_body(f"Relevant Coursework: {edu['coursework']}", italic=True,
                         size=int(cfg["font_size_body"] - 0.5))

    def render_skills():
        ts = data.get("technical_skills")
        fw = data.get("frameworks")
        ps = data.get("professional_skills")
        if not ts and not fw and not ps:
            return
        add_heading("Skills")
        tech_label = data.get("skills_label", "Technical Skills")
        if ts:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(cfg["space_after_body_pt"])
            r = p.add_run(f"{tech_label}:  ")
            r.font.bold = True
            r.font.name = cfg["font_body"]
            r.font.size = Pt(cfg["font_size_body"])
            r2 = p.add_run(ts)
            r2.font.name = cfg["font_body"]
            r2.font.size = Pt(cfg["font_size_body"])
            r2.font.color.rgb = hex_to_rgb(cfg["color_body"])
        if fw:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(cfg["space_after_body_pt"])
            r = p.add_run("Frameworks:  ")
            r.font.bold = True
            r.font.name = cfg["font_body"]
            r.font.size = Pt(cfg["font_size_body"])
            r2 = p.add_run(fw)
            r2.font.name = cfg["font_body"]
            r2.font.size = Pt(cfg["font_size_body"])
            r2.font.color.rgb = hex_to_rgb(cfg["color_body"])
        if ps:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(cfg["space_after_body_pt"])
            r = p.add_run("Professional Skills:  ")
            r.font.bold = True
            r.font.name = cfg["font_body"]
            r.font.size = Pt(cfg["font_size_body"])
            r2 = p.add_run(ps)
            r2.font.name = cfg["font_body"]
            r2.font.size = Pt(cfg["font_size_body"])
            r2.font.color.rgb = hex_to_rgb(cfg["color_body"])

    def render_certifications():
        if not data.get("certifications"):
            return
        add_heading("Certifications")
        for cert in data["certifications"]:
            add_body(f"{cert['name']}  |  {cert['issuer']}  |  {cert['year']}")

    def render_projects():
        if not data.get("projects"):
            return
        add_heading("Projects")
        for proj in data["projects"]:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(cfg["space_after_body_pt"])
            r = p.add_run(proj["name"] + ":  ")
            r.font.bold = True
            r.font.name = cfg["font_body"]
            r.font.size = Pt(cfg["font_size_body"])
            p.add_run(proj["description"]).font.size = Pt(cfg["font_size_body"])

    def render_volunteer():
        if not data.get("volunteer"):
            return
        add_heading("Volunteer Experience")
        for vol in data["volunteer"]:
            line = f"{vol['org']}  |  {vol['role']}  |  {vol['dates']}"
            add_body(line)
            for bullet in vol.get("bullets", []):
                add_bullet(bullet)

    def render_interests():
        if not cfg.get("include_interests_section"):
            return
        if not data.get("interests"):
            return
        add_heading("Interests")
        add_body(data["interests"])

    # ── Section order ──────────────────────────────────────────────────────────
    education_first = cfg.get("education_first", False) or data.get("education_first", False)

    render_summary()
    render_competencies()

    if education_first:
        render_education()
        if data.get("projects") and data.get("projects_before_experience"):
            render_projects()
        render_experience()
    else:
        render_experience()
        render_education()

    render_skills()
    render_certifications()

    if not (education_first and data.get("projects_before_experience")):
        render_projects()

    render_volunteer()
    render_interests()
```

---

### Entry point

```python
def generate_resume(data, template_number, output_path):
    """Generate a DOCX resume using the selected template config and save it."""
    cfg = load_config(template_number)

    doc = Document()
    for p in doc.paragraphs:
        p._element.getparent().remove(p._element)

    build_resume(doc, data, cfg)

    parent_dir = os.path.dirname(output_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    doc.save(output_path)
    print(f"Resume saved: {output_path}")


# ── Populate this dict from the user's answers ─────────────────────────────────
# Before filling in the data dict, derive these two flags:
#   is_student         = True if the user answered "yes" to question 3 (student/recent graduate)
#                        OR has fewer than 2 years of professional experience
#   education_first    = is_student or template_number == 7
#                        (students get education-first ordering regardless of which template they chose)
#   projects_before_experience = True if is_student AND the user has strong projects but limited work history

data = {
    "name":               "First Last",
    "email":              "email@example.com",
    "phone":              "+1 234 567 8900",
    "linkedin":           "https://linkedin.com/in/...",
    "github":             None,          # set to None if not provided
    "portfolio":          None,          # set to None if not provided
    "location":           "City, Country",
    "target_role":        "Senior Data Engineer",
    "is_student":         False,
    "is_executive":       False,
    "education_first":    False,
    "projects_before_experience": False,  # set True for entry-level with strong projects

    "summary": "Full summary or objective text here.",

    # Template 8 only — remove or set [] if not executive
    "competencies": [
        "Led enterprise data platform migration serving 4M daily users",
        "P&L accountability across $8M engineering budget",
    ],

    "experience": [
        {
            "company":  "Company Name",
            "title":    "Job Title",
            "dates":    "Jan 2022 – Present",
            "location": "Remote",
            "bullets":  [
                "Engineered a real-time pipeline using Kafka and dbt...",
                "Reduced query latency by 40% by redesigning...",
            ],
        },
    ],

    "education": [
        {
            "degree":      "BSc Computer Science",
            "institution": "University of Ghana",
            "year":        "2021",
            "field":       "Computer Science",
            "gpa":         None,          # include string like "3.7/4.0" only if 3.5+
            "coursework":  "Machine Learning, Databases, Cloud Computing",
        },
    ],

    "technical_skills":   "Python, SQL, dbt, Spark, Airflow, GCP, BigQuery",
    "professional_skills": "Cross-functional collaboration, stakeholder communication",
    "skills_label":        "Technical Skills",  # change for non-technical roles

    "certifications": [],
    "projects":       [],
    "volunteer":      [],
    "interests":      None,   # Template 3 only — e.g. "Distance running, West African jazz history, competitive chess"
}

template_number = TEMPLATE   # replace with the confirmed integer (1–8)

first, *rest = data["name"].split()
last = rest[-1] if rest else "Resume"
role_slug = data["target_role"].replace(" ", "-")
output_path = f"resume/tailored/{first}-{last}-{role_slug}.docx"

generate_resume(data, template_number, output_path)
```

---

## Phase 6: Final advisory and score

After generating the file, say this clearly:

"Before you submit this to any role:
- Read every line out loud — if it sounds like it was written by a robot, rewrite it in your own voice
- Verify every metric and achievement is accurate
- Check that the file name is professional: FirstName-LastName-Role.docx
- Remove any section that does not add value for this specific role
- To customise the template design (font, colors, sizes), edit the JSON file in resume/templates/configs/ and run /tailor-resume again"

Then run the resume match score (same logic as /score-resume) and display it at the bottom so the user knows where they stand before submitting.

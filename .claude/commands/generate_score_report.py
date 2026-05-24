#!/usr/bin/env python3
"""
generate_score_report.py
Generates a professional, non-editable PDF resume match score report.

Usage (called by Claude after running /score-resume):
    python3 .claude/commands/generate_score_report.py <data.json>
    python3 .claude/commands/generate_score_report.py --sample
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        HRFlowable, KeepTogether,
    )
    from reportlab.platypus.flowables import Flowable
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
    from reportlab.lib.pdfencrypt import StandardEncryption
except ImportError:
    print("reportlab is required. Run: pip3 install reportlab")
    sys.exit(1)

# ─── Colour palette ───────────────────────────────────────────────────────────
DARK        = colors.HexColor("#0E0E0E")
DARK2       = colors.HexColor("#1A1A1A")
ORANGE      = colors.HexColor("#E8611A")
ORANGE_MID  = colors.HexColor("#F0A050")
ORANGE_SOFT = colors.HexColor("#FFB380")
TEAL        = colors.HexColor("#16B2B2")
WHITE       = colors.white
OFF_WHITE   = colors.HexColor("#F8F8F8")
GREY_LIGHT  = colors.HexColor("#E4E4E4")
GREY_MID    = colors.HexColor("#AAAAAA")
GREY_BODY   = colors.HexColor("#444444")
GREY_NOTE   = colors.HexColor("#777777")

RATING_COLOURS = {
    "Weak":        colors.HexColor("#C0392B"),
    "Developing":  colors.HexColor("#D68910"),
    "Competitive": colors.HexColor("#1A7FC1"),
    "Strong":      TEAL,
    "Exceptional": colors.HexColor("#1E8449"),
}

# ─── Reviewer constants ───────────────────────────────────────────────────────
REVIEWER_NAME  = "Abigail Woolley"
REVIEWER_TITLE = "Job Search Strategist & ATS Analyst"
REVIEWER_BRAND = "The Job Search No One Taught You"
SERIES_URL     = (
    "https://www.linkedin.com/build-relation/newsletter-follow"
    "?entityUrn=7461467553941532672"
)

# ─── Sample data ──────────────────────────────────────────────────────────────
SAMPLE_DATA = {
    "candidate_name":     "Jane Doe",
    "candidate_email":    "jane.doe@email.com",
    "candidate_phone":    "+44 7700 123456",
    "candidate_linkedin": "https://linkedin.com/in/janedoe",
    "candidate_github":   "https://github.com/janedoe",
    "role_title":         "Senior Data Engineer",
    "company":            "Acme Corp",
    "date":               "",
    "scores": {
        "keyword_match":    {"score": 18, "max": 25},
        "skills_alignment": {"score": 15, "max": 20},
        "experience":       {"score": 20, "max": 25},
        "achievements":     {"score": 10, "max": 15},
        "structure_ats":    {"score":  8, "max": 10},
        "education":        {"score":  4, "max":  5},
    },
    "total": 75,
    "rating": "Competitive",
    "dimension_notes": {
        "keyword_match":
            "Missing: dbt, Airflow, Spark, data lakehouse, ELT pipelines",
        "skills_alignment":
            "Python and SQL present. dbt, Airflow, and GCP not mentioned.",
        "experience":
            "5 years relevant experience. Industry overlap is strong.",
        "achievements":
            "Some metrics present but 40% of bullets are task descriptions.",
        "structure_ats":
            "No tables or columns. Dates inconsistent in two roles.",
        "education":
            "Degree requirement met. No relevant certifications listed.",
    },
    "priority_1": [
        "Add missing ATS keywords: dbt, Airflow, Spark — include in Skills "
        "section and relevant bullets",
        "Add GCP experience or explicitly note cloud platform transferability",
        "Rewrite 3 task-description bullets as quantified achievements",
    ],
    "priority_2": [
        "Standardise date format across all roles (Month YYYY)",
        "Add a Professional Summary targeting this specific role",
    ],
    "priority_3": [
        "Add a Google Cloud or dbt certification to strengthen credentials",
        "Include a brief note on data lakehouse or modern data stack exposure",
    ],
}

DIMENSION_LABELS = {
    "keyword_match":    "Keyword Match",
    "skills_alignment": "Skills Alignment",
    "experience":       "Experience Relevance",
    "achievements":     "Achievement Quality",
    "structure_ats":    "Structure & ATS Safety",
    "education":        "Education & Credentials",
}


# ─── Custom flowables ─────────────────────────────────────────────────────────

class ScoreBar(Flowable):
    """Horizontal progress bar showing score / max in orange."""

    def __init__(self, score, max_score, width=95 * mm, height=7):
        """Initialise the bar with score, maximum value, and pixel dimensions."""
        Flowable.__init__(self)
        self.score     = score
        self.max_score = max_score
        self.bar_w     = width
        self.bar_h     = height
        self.width     = width
        self.height    = height + 2

    def draw(self):
        """Render the track and orange filled portion onto the canvas."""
        self.canv.setFillColor(GREY_LIGHT)
        self.canv.roundRect(0, 1, self.bar_w, self.bar_h, 3, fill=1, stroke=0)
        if self.max_score <= 0:
            return
        pct    = self.score / self.max_score
        filled = pct * self.bar_w
        pct_color = (
            ORANGE      if pct >= 0.8
            else colors.HexColor("#E8A020") if pct >= 0.6
            else colors.HexColor("#D9534F")
        )
        self.canv.setFillColor(pct_color)
        self.canv.roundRect(0, 1, filled, self.bar_h, 3, fill=1, stroke=0)


class DarkHeader(Flowable):
    """Full-width dark header drawn directly on the canvas."""

    def __init__(self, width, role_title, company, date_str,
                 total, rating, reviewer_name, reviewer_title):
        """Initialise with all header content fields."""
        Flowable.__init__(self)
        self.w              = width
        self.role_title     = role_title
        self.company        = company
        self.date_str       = date_str
        self.total          = total
        self.rating         = rating
        self.reviewer_name  = reviewer_name
        self.reviewer_title = reviewer_title
        self.height         = 64 * mm
        self.width          = width

    def draw(self):
        """Render the dark header with label, title, meta, score and reviewer."""
        c = self.canv
        w = self.w
        h = self.height

        # Background
        c.setFillColor(DARK)
        c.rect(0, 0, w, h, fill=1, stroke=0)

        # Orange bottom accent bar
        c.setFillColor(ORANGE)
        c.rect(0, 0, w, 4, fill=1, stroke=0)

        # ── Left column ───────────────────────────────────────────────────────
        c.setFillColor(ORANGE_SOFT)
        c.setFont("Helvetica", 7.5)
        c.drawString(0, h - 12 * mm, "THE JOB SEARCH NO ONE TAUGHT YOU")

        # Role title
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 20)
        title = self.role_title
        if len(title) > 36:
            title = title[:34] + "…"
        c.drawString(0, h - 23 * mm, title)

        # Company + date
        c.setFillColor(GREY_MID)
        c.setFont("Helvetica", 9)
        c.drawString(0, h - 31 * mm,
                     f"{self.company}  ·  {self.date_str}")

        # Thin divider
        c.setStrokeColor(colors.HexColor("#333333"))
        c.setLineWidth(0.5)
        c.line(0, h - 37 * mm, w * 0.56, h - 37 * mm)

        # Reviewer credit
        c.setFillColor(GREY_MID)
        c.setFont("Helvetica", 8)
        c.drawString(0, h - 44 * mm, "Reviewed by")
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(22 * mm, h - 44 * mm, self.reviewer_name)
        c.setFillColor(GREY_MID)
        c.setFont("Helvetica", 7.5)
        c.drawString(0, h - 51 * mm, self.reviewer_title)

        # ── Right column — score badge ────────────────────────────────────────
        r_col = RATING_COLOURS.get(self.rating, TEAL)

        # Rating label
        c.setFillColor(r_col)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawRightString(w, h - 12 * mm, self.rating.upper())

        # Big score number
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 50)
        c.drawRightString(w - 14 * mm, h - 35 * mm, str(self.total))

        # "/ 100"
        c.setFillColor(GREY_MID)
        c.setFont("Helvetica", 15)
        c.drawString(w - 12 * mm, h - 35 * mm, "/ 100")

        # Caption
        c.setFillColor(GREY_MID)
        c.setFont("Helvetica", 7)
        c.drawRightString(w, h - 44 * mm, "OVERALL SCORE")


class WatermarkFlowable(Flowable):
    """Zero-height flowable that draws a diagonal branded watermark on the page."""

    def __init__(self, reviewer_name, reviewer_title):
        """Initialise with reviewer credit text."""
        Flowable.__init__(self)
        self.reviewer_name  = reviewer_name
        self.reviewer_title = reviewer_title
        self.width  = 0
        self.height = 0

    def draw(self):
        """Draw a faint diagonal watermark across the current page."""
        c = self.canv
        c.saveState()
        c.translate(A4[0] / 2, A4[1] / 2)
        c.rotate(42)
        c.setFillColor(colors.Color(0.87, 0.87, 0.87))
        c.setFont("Helvetica-Bold", 32)
        c.drawCentredString(0, 12, self.reviewer_name)
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.Color(0.87, 0.87, 0.87))
        c.drawCentredString(0, -10, self.reviewer_title)
        c.restoreState()


# ─── Style helper ─────────────────────────────────────────────────────────────

def _s(name, **kw):
    """Create and return a named ParagraphStyle with the given attributes."""
    return ParagraphStyle(name, **kw)


# ─── PDF builder ──────────────────────────────────────────────────────────────

def build_report(data: dict, output_path: str):
    """Build and save the PDF score report from a structured data dictionary.

    Args:
        data: Score data dict containing candidate info, dimension scores,
              dimension notes, and priority action items. See SAMPLE_DATA
              for the expected schema.
        output_path: Absolute or relative path where the PDF will be saved.
    """
    date_str = data.get("date") or datetime.now().strftime("%d %B %Y")
    total    = data.get("total",
                        sum(v["score"] for v in data["scores"].values()))
    rating   = data.get("rating", "Competitive")

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=10 * mm,
        bottomMargin=18 * mm,
        title="Resume Match Score Report",
        author=REVIEWER_NAME,
        subject=f"Resume score for {data.get('candidate_name', 'Candidate')}",
        creator=f"{REVIEWER_NAME} via Job Search AI Kit",
        producer="Job Search AI Kit",
        encrypt=StandardEncryption(
            "", canPrint=1, canModify=0, canCopy=0, canAnnotate=0
        ),
    )

    W     = A4[0] - 36 * mm
    story = []

    # ── PAGE WATERMARK ────────────────────────────────────────────────────────
    story.append(WatermarkFlowable(REVIEWER_NAME, REVIEWER_TITLE))

    # ── DARK HEADER ───────────────────────────────────────────────────────────
    story.append(DarkHeader(
        width          = W,
        role_title     = data.get("role_title", "Role"),
        company        = data.get("company", ""),
        date_str       = date_str,
        total          = total,
        rating         = rating,
        reviewer_name  = REVIEWER_NAME,
        reviewer_title = REVIEWER_TITLE,
    ))
    story.append(Spacer(1, 6 * mm))

    # ── CANDIDATE NAME + CONTACT LINKS ───────────────────────────────────────
    cname   = data.get("candidate_name", "")
    c_email = data.get("candidate_email", "")
    c_phone = data.get("candidate_phone", "")
    c_li    = data.get("candidate_linkedin", "")
    c_gh    = data.get("candidate_github", "")

    if cname:
        story.append(Paragraph(
            cname,
            _s("cn", fontName="Helvetica-Bold", fontSize=11,
               textColor=DARK, leading=14),
        ))
        story.append(Spacer(1, 1.5 * mm))

    contact_parts = []
    if c_email:
        contact_parts.append(
            f'<link href="mailto:{c_email}">{c_email}</link>')
    if c_phone:
        tel_uri = re.sub(r"[\s\-()]", "", c_phone)
        contact_parts.append(
            f'<link href="tel:{tel_uri}">{c_phone}</link>')
    if c_li:
        contact_parts.append(
            f'<link href="{c_li}">LinkedIn Profile</link>')
    if c_gh:
        contact_parts.append(
            f'<link href="{c_gh}">GitHub Portfolio</link>')
    if contact_parts:
        story.append(Paragraph(
            "  ·  ".join(contact_parts),
            _s("cl", fontName="Helvetica", fontSize=8.5,
               textColor=TEAL, leading=12),
        ))
    story.append(Spacer(1, 6 * mm))

    # ── SCORE BREAKDOWN ───────────────────────────────────────────────────────
    story.append(Paragraph(
        "SCORE BREAKDOWN",
        _s("sh", fontName="Helvetica-Bold", fontSize=7.5,
           textColor=ORANGE, leading=10, letterSpacing=1.5,
           spaceAfter=2 * mm),
    ))

    bar_w = 85 * mm
    rows  = []
    for key, label in DIMENSION_LABELS.items():
        entry = data["scores"].get(key, {"score": 0, "max": 0})
        sc, mx = entry["score"], entry["max"]
        rows.append([
            Paragraph(label,
                      _s(f"sl{key}", fontName="Helvetica", fontSize=9,
                         textColor=GREY_BODY, leading=12)),
            ScoreBar(sc, mx, width=bar_w, height=7),
            Paragraph(
                f"<b>{sc}</b><font color='#AAAAAA'> / {mx}</font>",
                _s(f"sn{key}", fontName="Helvetica", fontSize=9,
                   textColor=DARK, leading=12, alignment=TA_RIGHT)),
        ])

    score_tbl = Table(rows,
                      colWidths=[50 * mm, bar_w, 20 * mm],
                      rowHeights=[9 * mm] * len(rows))
    score_tbl.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 0), (-1, -1), [OFF_WHITE, WHITE]),
        ("LEFTPADDING",   (0, 0), (-1, -1), 3 * mm),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 3 * mm),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LINEBELOW",     (0, -1), (-1, -1), 0.5, GREY_LIGHT),
    ]))
    story.append(score_tbl)
    story.append(Spacer(1, 7 * mm))

    # ── DIMENSION NOTES ───────────────────────────────────────────────────────
    notes     = data.get("dimension_notes", {})
    note_rows = [(k, notes[k]) for k in DIMENSION_LABELS if notes.get(k)]
    if note_rows:
        story.append(Paragraph(
            "DIMENSION NOTES",
            _s("nh", fontName="Helvetica-Bold", fontSize=7.5,
               textColor=ORANGE, leading=10, letterSpacing=1.5,
               spaceAfter=2 * mm),
        ))
        nt_data = [[
            Paragraph(DIMENSION_LABELS[k],
                      _s(f"nl{k}", fontName="Helvetica-Bold", fontSize=8.5,
                         textColor=DARK, leading=13)),
            Paragraph(v,
                      _s(f"nv{k}", fontName="Helvetica-Oblique", fontSize=8.5,
                         textColor=GREY_NOTE, leading=13)),
        ] for k, v in note_rows]
        nt = Table(nt_data, colWidths=[50 * mm, W - 50 * mm])
        nt.setStyle(TableStyle([
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("ROWBACKGROUNDS",(0, 0), (-1, -1), [OFF_WHITE, WHITE]),
            ("LEFTPADDING",   (0, 0), (-1, -1), 3 * mm),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 3 * mm),
            ("TOPPADDING",    (0, 0), (-1, -1), 2.5 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ]))
        story.append(nt)
        story.append(Spacer(1, 7 * mm))

    # ── ACTION PLAN ───────────────────────────────────────────────────────────
    story.append(Paragraph(
        "ACTION PLAN",
        _s("ap", fontName="Helvetica-Bold", fontSize=7.5,
           textColor=ORANGE, leading=10, letterSpacing=1.5,
           spaceAfter=2 * mm),
    ))

    priorities = [
        ("priority_1", "PRIORITY 1", "Do this before applying",
         ORANGE),
        ("priority_2", "PRIORITY 2", "Strongly recommended",
         DARK2),
        ("priority_3", "PRIORITY 3", "Nice to have",
         colors.HexColor("#555555")),
    ]

    for key, label, subtitle, accent in priorities:
        items = data.get(key, [])
        if not items:
            continue
        block = []
        hdr = Table([[
            Paragraph(label,
                      _s(f"pl{key}", fontName="Helvetica-Bold", fontSize=8.5,
                         textColor=WHITE, leading=12)),
            Paragraph(subtitle,
                      _s(f"ps{key}", fontName="Helvetica", fontSize=8,
                         textColor=colors.HexColor("#CCCCCC"),
                         leading=12, alignment=TA_RIGHT)),
        ]], colWidths=[W * 0.4, W * 0.6])
        hdr.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), accent),
            ("LEFTPADDING",   (0, 0), (0, 0),   4 * mm),
            ("RIGHTPADDING",  (1, 0), (1, 0),   4 * mm),
            ("TOPPADDING",    (0, 0), (-1, -1), 2.5 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5 * mm),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ]))
        block.append(hdr)
        for item in items:
            block.append(Paragraph(
                f"<bullet>&bull;</bullet> {item}",
                _s(f"bi{key}", fontName="Helvetica", fontSize=9,
                   textColor=GREY_BODY, leading=14,
                   leftIndent=10 * mm, firstLineIndent=-6 * mm,
                   spaceBefore=2 * mm),
            ))
        block.append(Spacer(1, 5 * mm))
        story.append(KeepTogether(block))

    # ── FOOTER ────────────────────────────────────────────────────────────────
    story.append(Spacer(1, 3 * mm))
    story.append(HRFlowable(
        width="100%", thickness=0.75,
        color=GREY_LIGHT, spaceAfter=3 * mm,
    ))
    footer = Table([[
        Paragraph(
            f"<b>{REVIEWER_NAME}</b>  ·  {REVIEWER_TITLE}  ·  "
            f"Generated {date_str}",
            _s("fl", fontName="Helvetica", fontSize=7.5,
               textColor=GREY_MID, leading=11),
        ),
        Paragraph(
            f'<link href="{SERIES_URL}">'
            f'<font color="#16B2B2">Follow the series: '
            f'{REVIEWER_BRAND}</font></link>',
            _s("fr", fontName="Helvetica", fontSize=7.5,
               textColor=GREY_MID, leading=11, alignment=TA_RIGHT),
        ),
    ]], colWidths=[W * 0.5, W * 0.5])
    footer.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(footer)

    doc.build(story)
    print(f"Report saved: {output_path}")


# ─── Entry point ──────────────────────────────────────────────────────────────

def main():
    """Parse CLI arguments and invoke build_report with the supplied data file."""
    if len(sys.argv) < 2:
        print("Usage: python3 generate_score_report.py <data.json>")
        print("       python3 generate_score_report.py --sample")
        sys.exit(1)

    if sys.argv[1] == "--sample":
        data = SAMPLE_DATA
        out  = "score_report_sample.pdf"
    else:
        with open(sys.argv[1]) as f:
            data = json.load(f)
        base = str(Path(sys.argv[1]).with_suffix(""))
        out  = data.get("output_path") or f"{base}_report.pdf"

    build_report(data, out)


if __name__ == "__main__":
    main()

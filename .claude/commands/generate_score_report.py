#!/usr/bin/env python3
"""
generate_score_report.py
Generates a professional, non-editable PDF resume match score report.

Usage (called by Claude after running /score-resume):
    python3 .claude/commands/generate_score_report.py <data.json>

The data.json must contain the fields shown in SAMPLE_DATA below.
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
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import mm, cm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        HRFlowable, KeepTogether
    )
    from reportlab.platypus.flowables import Flowable
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
    from reportlab.graphics.shapes import Drawing, Circle, Rect, String
    from reportlab.graphics import renderPDF
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.pdfencrypt import StandardEncryption
except ImportError:
    print("reportlab is required. Run: pip3 install reportlab")
    sys.exit(1)

# ─── Brand colours ────────────────────────────────────────────────────────────
DARK       = colors.HexColor("#0E0E0E")
ORANGE     = colors.HexColor("#E8611A")
TEAL       = colors.HexColor("#16B2B2")
GOLD       = colors.HexColor("#FFC857")
WHITE      = colors.white
OFF_WHITE  = colors.HexColor("#F7F7F7")
GREY_TEXT  = colors.HexColor("#555555")
GREY_LIGHT = colors.HexColor("#E8E8E8")
GREY_MID   = colors.HexColor("#AAAAAA")

RATING_COLOURS = {
    "Weak":        colors.HexColor("#D9534F"),
    "Developing":  colors.HexColor("#E8A020"),
    "Competitive": colors.HexColor("#F0C040"),
    "Strong":      colors.HexColor("#5CB85C"),
    "Exceptional": colors.HexColor("#16B2B2"),
}

# ─── Reviewer details ─────────────────────────────────────────────────────────
REVIEWER_NAME  = "Abigail Woolley"
REVIEWER_TITLE = "Job Search Strategist & ATS Analyst"
REVIEWER_BRAND = "The Job Search No One Taught You"
PHOTO_PATH     = Path(__file__).parent / "reviewer_photo.png"

# ─── Sample data structure ────────────────────────────────────────────────────
SAMPLE_DATA = {
    "candidate_name": "Jane Doe",
    "candidate_email": "jane.doe@email.com",
    "candidate_phone": "+44 7700 123456",
    "candidate_linkedin": "https://linkedin.com/in/janedoe",
    "candidate_github": "https://github.com/janedoe",
    "role_title": "Senior Data Engineer",
    "company": "Acme Corp",
    "date": "",           # leave blank to auto-fill today
    "scores": {
        "keyword_match":     {"score": 18, "max": 25},
        "skills_alignment":  {"score": 15, "max": 20},
        "experience":        {"score": 20, "max": 25},
        "achievements":      {"score": 10, "max": 15},
        "structure_ats":     {"score":  8, "max": 10},
        "education":         {"score":  4, "max":  5},
    },
    "total": 75,
    "rating": "Competitive",
    "dimension_notes": {
        "keyword_match":    "Missing: dbt, Airflow, Spark, data lakehouse, ELT pipelines",
        "skills_alignment": "Python and SQL present. dbt, Airflow, and GCP not mentioned.",
        "experience":       "5 years relevant experience. Industry overlap is strong.",
        "achievements":     "Some metrics present but 40% of bullets are task descriptions.",
        "structure_ats":    "No tables or columns. Dates inconsistent in two roles.",
        "education":        "Degree requirement met. No relevant certifications listed.",
    },
    "priority_1": [
        "Add missing ATS keywords: dbt, Airflow, Spark — in Skills section and relevant bullets",
        "Add GCP experience or note cloud platform transferability explicitly",
        "Rewrite 3 task-description bullets with quantified outcomes",
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


# ─── Custom flowables ─────────────────────────────────────────────────────────

class ScoreBar(Flowable):
    """Horizontal progress bar showing score / max."""

    def __init__(self, score, max_score, width=120, height=10):
        """Initialise the bar with score, maximum value, and pixel dimensions."""
        Flowable.__init__(self)
        self.score = score
        self.max_score = max_score
        self.bar_w = width
        self.bar_h = height
        self.width = width
        self.height = height + 2

    def draw(self):
        """Render the track and filled portion onto the canvas."""
        # Always draw the empty track
        self.canv.setFillColor(GREY_LIGHT)
        self.canv.roundRect(0, 1, self.bar_w, self.bar_h, 3, fill=1, stroke=0)
        # Guard against divide-by-zero; skip fill if max_score is invalid
        if self.max_score <= 0:
            return
        pct = self.score / self.max_score
        filled = pct * self.bar_w
        fill_color = (
            ORANGE if pct >= 0.8
            else colors.HexColor("#E8A020") if pct >= 0.6
            else colors.HexColor("#D9534F")
        )
        self.canv.setFillColor(fill_color)
        self.canv.roundRect(0, 1, filled, self.bar_h, 3, fill=1, stroke=0)


class HeaderBand(Flowable):
    """Full-width dark header with orange accent line at the bottom."""

    def __init__(self, page_width, height=62*mm):
        """Initialise the band with the full page width and desired height."""
        Flowable.__init__(self)
        self.page_width = page_width
        self.height = height
        self.width = page_width

    def draw(self):
        """Render the dark background rectangle and orange bottom accent."""
        # Dark background
        self.canv.setFillColor(DARK)
        self.canv.rect(0, 0, self.page_width, self.height, fill=1, stroke=0)
        # Orange accent bar at bottom
        self.canv.setFillColor(ORANGE)
        self.canv.rect(0, 0, self.page_width, 4, fill=1, stroke=0)


class CirclePhoto(Flowable):
    """Draws the reviewer photo clipped to a circle with an orange border."""

    def __init__(self, path, diameter=38*mm):
        """Initialise with the image file path and circle diameter in points."""
        Flowable.__init__(self)
        self.path = str(path)
        self.d = diameter
        self.width = diameter
        self.height = diameter

    def draw(self):
        """Render the orange border ring and clip the image to a circle."""
        if not os.path.exists(self.path):
            return
        r = self.d / 2
        # Orange ring
        self.canv.setFillColor(ORANGE)
        self.canv.circle(r, r, r + 1.5*mm, fill=1, stroke=0)
        # Clip circle and draw image
        self.canv.saveState()
        p = self.canv.beginPath()
        p.circle(r, r, r)
        self.canv.clipPath(p, stroke=0)
        self.canv.drawImage(
            self.path, 0, 0, width=self.d, height=self.d,
            preserveAspectRatio=True, anchor='c', mask='auto'
        )
        self.canv.restoreState()


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

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=18*mm,
        rightMargin=18*mm,
        topMargin=12*mm,
        bottomMargin=16*mm,
        title="Resume Match Score Report",
        author=REVIEWER_NAME,
        subject=f"Resume score for {data.get('candidate_name', 'Candidate')}",
        creator=f"{REVIEWER_NAME} via Job Search AI Kit",
        producer="Job Search AI Kit",
        # Empty user password (open freely) + owner password locks editing.
        # canPrint=1 allows printing; canModify=0 disables editing in viewers.
        encrypt=StandardEncryption("", canPrint=1, canModify=0,
                                   canCopy=0, canAnnotate=0),
    )

    styles = getSampleStyleSheet()
    W = A4[0] - 36*mm  # usable width

    def style(name, **kw):
        """Create and return a named ParagraphStyle with the given attributes."""
        s = ParagraphStyle(name, **kw)
        return s

    S_LABEL = style("label",
        fontName="Helvetica-Bold", fontSize=7,
        textColor=ORANGE, spaceAfter=1*mm, leading=10,
        letterSpacing=1.5)
    S_H1 = style("h1",
        fontName="Helvetica-Bold", fontSize=20,
        textColor=WHITE, leading=24)
    S_SUBHEAD = style("subhead",
        fontName="Helvetica", fontSize=10,
        textColor=GREY_MID, leading=14)
    S_SECTION = style("section",
        fontName="Helvetica-Bold", fontSize=11,
        textColor=DARK, spaceBefore=5*mm, spaceAfter=2*mm)
    S_BODY = style("body",
        fontName="Helvetica", fontSize=9.5,
        textColor=GREY_TEXT, leading=15)
    S_BULLET = style("bullet",
        fontName="Helvetica", fontSize=9.5,
        textColor=GREY_TEXT, leading=15,
        leftIndent=10, firstLineIndent=-10,
        spaceBefore=1.5*mm)
    S_NOTE = style("note",
        fontName="Helvetica-Oblique", fontSize=8.5,
        textColor=GREY_MID, leading=13)
    S_SCORE_LABEL = style("score_label",
        fontName="Helvetica-Bold", fontSize=9,
        textColor=DARK, leading=12)
    S_SCORE_NUM = style("score_num",
        fontName="Helvetica-Bold", fontSize=9,
        textColor=ORANGE, leading=12, alignment=TA_RIGHT)
    S_RATING = style("rating",
        fontName="Helvetica-Bold", fontSize=26,
        textColor=DARK, leading=30)
    S_TOTAL = style("total",
        fontName="Helvetica-Bold", fontSize=14,
        textColor=DARK, leading=18)
    S_FOOTER = style("footer",
        fontName="Helvetica", fontSize=7.5,
        textColor=GREY_MID, alignment=TA_CENTER, leading=11)
    S_PRIORITY = style("priority",
        fontName="Helvetica-Bold", fontSize=10,
        textColor=WHITE, leading=13)

    story = []

    # ── HEADER ────────────────────────────────────────────────────────────────
    # Two-column header: left = text, right = photo
    photo_d = 36*mm
    text_w  = W - photo_d - 6*mm

    left_cells = [
        Paragraph("RESUME MATCH SCORE REPORT", S_LABEL),
        Spacer(1, 2*mm),
        Paragraph(
            data.get("role_title", "Role"),
            style("h1big", fontName="Helvetica-Bold", fontSize=18,
                  textColor=WHITE, leading=22)
        ),
        Spacer(1, 1.5*mm),
        Paragraph(
            f"{data.get('company', '')}  &nbsp;·&nbsp;  Reviewed {date_str}",
            S_SUBHEAD
        ),
        Spacer(1, 2*mm),
        Paragraph(
            f"<b><font color='#FFFFFF'>{REVIEWER_NAME}</font></b>"
            f"  <font color='#AAAAAA'>·  {REVIEWER_TITLE}</font>",
            style("rev", fontName="Helvetica", fontSize=8.5,
                  textColor=GREY_MID, leading=12)
        ),
    ]

    header_table = Table(
        [[left_cells, CirclePhoto(PHOTO_PATH, photo_d)]],
        colWidths=[text_w, photo_d],
        rowHeights=[58*mm],
    )
    header_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK),
        ("VALIGN",     (0, 0), (0, 0),   "MIDDLE"),
        ("VALIGN",     (1, 0), (1, 0),   "MIDDLE"),
        ("ALIGN",      (1, 0), (1, 0),   "CENTER"),
        ("LEFTPADDING",  (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 4*mm),
        ("TOPPADDING",   (0, 0), (-1, -1), 10*mm),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 8*mm),
    ]))
    story.append(header_table)

    # Orange accent line
    story.append(HRFlowable(width="100%", thickness=4, color=ORANGE, spaceAfter=5*mm))

    # ── CANDIDATE INFO + CONTACT LINKS ───────────────────────────────────────
    S_LINK = style("link",
        fontName="Helvetica", fontSize=9,
        textColor=TEAL, leading=13)

    cname   = data.get("candidate_name", "")
    c_email = data.get("candidate_email", "")
    c_phone = data.get("candidate_phone", "")
    c_li    = data.get("candidate_linkedin", "")
    c_gh    = data.get("candidate_github", "")

    if cname:
        story.append(Paragraph(f"Candidate: <b>{cname}</b>", S_BODY))
        story.append(Spacer(1, 2*mm))

    # Build contact link chips — only include fields that are present
    contact_parts = []
    if c_email:
        contact_parts.append(
            f'<link href="mailto:{c_email}">&#x2709; {c_email}</link>'
        )
    if c_phone:
        # Strip spaces/dashes for the tel: URI
        tel_uri = re.sub(r"[\s\-()]", "", c_phone)
        contact_parts.append(
            f'<link href="tel:{tel_uri}">&#x260E; {c_phone}</link>'
        )
    if c_li:
        contact_parts.append(
            f'<link href="{c_li}">LinkedIn Profile</link>'
        )
    if c_gh:
        contact_parts.append(
            f'<link href="{c_gh}">GitHub Portfolio</link>'
        )

    if contact_parts:
        story.append(
            Paragraph("  ·  ".join(contact_parts), S_LINK)
        )
        story.append(Spacer(1, 5*mm))

    # ── SCORE TABLE ───────────────────────────────────────────────────────────
    story.append(Paragraph("SCORE BREAKDOWN", S_LABEL))
    story.append(Spacer(1, 1.5*mm))

    dimension_labels = {
        "keyword_match":    "Keyword Match",
        "skills_alignment": "Skills Alignment",
        "experience":       "Experience Relevance",
        "achievements":     "Achievement Quality",
        "structure_ats":    "Structure & ATS Safety",
        "education":        "Education & Credentials",
    }

    bar_w = 90*mm
    rows = []
    for key, label in dimension_labels.items():
        entry = data["scores"].get(key, {"score": 0, "max": 0})
        sc, mx = entry["score"], entry["max"]
        rows.append([
            Paragraph(label, S_SCORE_LABEL),
            ScoreBar(sc, mx, width=bar_w, height=8),
            Paragraph(f"{sc} / {mx}", S_SCORE_NUM),
        ])

    score_table = Table(
        rows,
        colWidths=[52*mm, bar_w, 18*mm],
        rowHeights=[9*mm] * len(rows),
    )
    score_table.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 0), (-1, -1), [OFF_WHITE, WHITE]),
        ("LEFTPADDING",   (0, 0), (-1, -1), 3*mm),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 3*mm),
        ("TOPPADDING",    (0, 0), (-1, -1), 1*mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1*mm),
    ]))
    story.append(score_table)
    story.append(Spacer(1, 4*mm))

    # ── TOTAL + RATING ────────────────────────────────────────────────────────
    total = data.get("total", sum(
        v["score"] for v in data["scores"].values()
    ))
    rating = data.get("rating", "Competitive")
    rating_color = RATING_COLOURS.get(rating, ORANGE)

    total_table = Table(
        [[
            Paragraph(f"TOTAL SCORE  <b>{total} / 100</b>", S_TOTAL),
            Paragraph(
                f"<font color='{rating_color.hexval()}'>{rating}</font>",
                style("rt", fontName="Helvetica-Bold", fontSize=22,
                      textColor=rating_color, leading=26, alignment=TA_RIGHT)
            ),
        ]],
        colWidths=[W * 0.55, W * 0.45],
    )
    total_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), DARK),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING",   (0, 0), (0, 0),   4*mm),
        ("RIGHTPADDING",  (1, 0), (1, 0),   4*mm),
        ("TOPPADDING",    (0, 0), (-1, -1), 3.5*mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5*mm),
    ]))
    story.append(total_table)
    story.append(Spacer(1, 6*mm))

    # ── DIMENSION NOTES ───────────────────────────────────────────────────────
    notes = data.get("dimension_notes", {})
    if notes:
        story.append(Paragraph("DIMENSION NOTES", S_LABEL))
        story.append(Spacer(1, 1.5*mm))
        note_rows = []
        for key, label in dimension_labels.items():
            note = notes.get(key, "")
            if note:
                note_rows.append([
                    Paragraph(label, S_SCORE_LABEL),
                    Paragraph(note, S_NOTE),
                ])
        if note_rows:
            note_table = Table(note_rows, colWidths=[52*mm, W - 52*mm])
            note_table.setStyle(TableStyle([
                ("VALIGN",        (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS",(0, 0), (-1, -1), [OFF_WHITE, WHITE]),
                ("LEFTPADDING",   (0, 0), (-1, -1), 3*mm),
                ("RIGHTPADDING",  (0, 0), (-1, -1), 3*mm),
                ("TOPPADDING",    (0, 0), (-1, -1), 2*mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2*mm),
            ]))
            story.append(note_table)
            story.append(Spacer(1, 6*mm))

    # ── ACTION PLAN ───────────────────────────────────────────────────────────
    priorities = [
        ("priority_1", "PRIORITY 1", "Do this before applying", ORANGE),
        ("priority_2", "PRIORITY 2", "Strongly recommended",    TEAL),
        ("priority_3", "PRIORITY 3", "Nice to have",            GREY_MID),
    ]

    story.append(Paragraph("ACTION PLAN", S_LABEL))
    story.append(Spacer(1, 1.5*mm))

    for key, label, sub, col in priorities:
        items = data.get(key, [])
        if not items:
            continue
        block = []
        # Priority header
        hdr = Table(
            [[
                Paragraph(label, style("pl", fontName="Helvetica-Bold",
                                       fontSize=9, textColor=WHITE, leading=12)),
                Paragraph(sub,  style("ps", fontName="Helvetica",
                                      fontSize=8.5, textColor=WHITE,
                                      leading=12, alignment=TA_RIGHT)),
            ]],
            colWidths=[W * 0.4, W * 0.6],
        )
        hdr.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), col),
            ("LEFTPADDING",   (0, 0), (0, 0),   3*mm),
            ("RIGHTPADDING",  (1, 0), (1, 0),   3*mm),
            ("TOPPADDING",    (0, 0), (-1, -1), 2*mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2*mm),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ]))
        block.append(hdr)
        for item in items:
            block.append(
                Paragraph(f"<bullet>•</bullet> {item}", S_BULLET)
            )
        block.append(Spacer(1, 4*mm))
        story.append(KeepTogether(block))

    # ── FOOTER ────────────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1, color=GREY_LIGHT,
                             spaceBefore=4*mm, spaceAfter=3*mm))
    story.append(Paragraph(
        f"{REVIEWER_NAME}  ·  {REVIEWER_TITLE}  ·  {REVIEWER_BRAND}  "
        f"·  Generated {date_str}",
        S_FOOTER
    ))
    story.append(Paragraph(
        "This report was generated using the Job Search AI Kit. "
        "All analysis is for guidance only.",
        style("disc", fontName="Helvetica-Oblique", fontSize=7,
              textColor=GREY_LIGHT, alignment=TA_CENTER, leading=10)
    ))

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
        out = "score_report_sample.pdf"
    else:
        with open(sys.argv[1]) as f:
            data = json.load(f)
        base = str(Path(sys.argv[1]).with_suffix(""))
        out = data.get("output_path") or f"{base}_report.pdf"

    build_report(data, out)


if __name__ == "__main__":
    main()

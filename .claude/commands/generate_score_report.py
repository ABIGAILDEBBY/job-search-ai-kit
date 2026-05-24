#!/usr/bin/env python3
"""
generate_score_report.py
Generates a professional, non-editable PDF resume match score report.

Usage (called by Claude after running /score-resume):
    python3 .claude/commands/generate_score_report.py <data.json>
    python3 .claude/commands/generate_score_report.py --sample

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
        HRFlowable, KeepTogether, Frame, PageTemplate
    )
    from reportlab.platypus.flowables import Flowable
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
    from reportlab.pdfbase import pdfmetrics
    from reportlab.lib.pdfencrypt import StandardEncryption
except ImportError:
    print("reportlab is required. Run: pip3 install reportlab")
    sys.exit(1)

# ─── Colour palette (professional: charcoal, teal, white, greys) ──────────────
INK        = colors.HexColor("#1C1C1C")   # near-black for headlines
TEAL       = colors.HexColor("#16B2B2")   # primary accent
TEAL_DARK  = colors.HexColor("#0E8080")   # darker teal for hover/contrast
WHITE      = colors.white
PAGE_BG    = colors.white
BAND_BG    = colors.HexColor("#F4F6F7")   # very light grey for alternating rows
RULE       = colors.HexColor("#DCDCDC")   # horizontal rules
GREY_LABEL = colors.HexColor("#888888")   # meta labels
GREY_BODY  = colors.HexColor("#444444")   # body text
GREY_NOTE  = colors.HexColor("#777777")   # dimension notes
SCORE_FILL = TEAL                          # progress bar fill
SCORE_TRACK= colors.HexColor("#E4E4E4")   # progress bar track

RATING_COLOURS = {
    "Weak":        colors.HexColor("#C0392B"),
    "Developing":  colors.HexColor("#D68910"),
    "Competitive": colors.HexColor("#1A7FC1"),
    "Strong":      TEAL,
    "Exceptional": colors.HexColor("#1E8449"),
}

# ─── Reviewer constants ────────────────────────────────────────────────────────
REVIEWER_NAME   = "Abigail Woolley"
REVIEWER_TITLE  = "Job Search Strategist & ATS Analyst"
REVIEWER_BRAND  = "The Job Search No One Taught You"
SERIES_URL      = "https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7461467553941532672"
PHOTO_PATH      = Path(__file__).parent / "reviewer_photo.png"

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
        "keyword_match":    "Missing: dbt, Airflow, Spark, data lakehouse, ELT pipelines",
        "skills_alignment": "Python and SQL present. dbt, Airflow, and GCP not mentioned.",
        "experience":       "5 years relevant experience. Industry overlap is strong.",
        "achievements":     "Some metrics present but 40% of bullets are task descriptions.",
        "structure_ats":    "No tables or columns. Dates inconsistent in two roles.",
        "education":        "Degree requirement met. No relevant certifications listed.",
    },
    "priority_1": [
        "Add missing ATS keywords: dbt, Airflow, Spark — include in Skills section and relevant bullets",
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

# ─── Custom flowables ─────────────────────────────────────────────────────────

class TealBar(Flowable):
    """A full-width teal rule used as a top-of-page accent stripe."""

    def __init__(self, width, height=3):
        """Initialise with page width and bar height in points."""
        Flowable.__init__(self)
        self.bar_w = width
        self.bar_h = height
        self.width = width
        self.height = height

    def draw(self):
        """Render the teal stripe onto the canvas."""
        self.canv.setFillColor(TEAL)
        self.canv.rect(0, 0, self.bar_w, self.bar_h, fill=1, stroke=0)


class ScoreBar(Flowable):
    """Horizontal progress bar showing score / max in teal."""

    def __init__(self, score, max_score, width=100*mm, height=6):
        """Initialise the bar with score, maximum value, and pixel dimensions."""
        Flowable.__init__(self)
        self.score     = score
        self.max_score = max_score
        self.bar_w     = width
        self.bar_h     = height
        self.width     = width
        self.height    = height + 2

    def draw(self):
        """Render the track and filled portion onto the canvas."""
        # Track
        self.canv.setFillColor(SCORE_TRACK)
        self.canv.roundRect(0, 1, self.bar_w, self.bar_h, 2, fill=1, stroke=0)
        # Guard against divide-by-zero
        if self.max_score <= 0:
            return
        pct    = self.score / self.max_score
        filled = pct * self.bar_w
        self.canv.setFillColor(SCORE_FILL)
        self.canv.roundRect(0, 1, filled, self.bar_h, 2, fill=1, stroke=0)


class ReviewerStamp(Flowable):
    """Small inline reviewer block: circular photo + name + title."""

    def __init__(self, photo_path, diameter=14*mm, text_lines=None):
        """Initialise with photo path, circle size, and text lines to render."""
        Flowable.__init__(self)
        self.photo_path = str(photo_path)
        self.d          = diameter
        self.text_lines = text_lines or []
        self.width      = 200*mm
        self.height     = diameter + 2*mm

    def draw(self):
        """Render the small circular photo and reviewer text side by side."""
        r = self.d / 2
        if os.path.exists(self.photo_path):
            # Thin teal ring
            self.canv.setFillColor(TEAL)
            self.canv.circle(r, r, r + 1*mm, fill=1, stroke=0)
            # Clip to circle and draw image
            self.canv.saveState()
            p = self.canv.beginPath()
            p.circle(r, r, r)
            self.canv.clipPath(p, stroke=0)
            self.canv.drawImage(
                self.photo_path, 0, 0,
                width=self.d, height=self.d,
                preserveAspectRatio=True, anchor="c", mask="auto",
            )
            self.canv.restoreState()
        # Text to the right of the photo
        tx = self.d + 4*mm
        ty = self.d - 3*mm
        for i, (text, font, size, col) in enumerate(self.text_lines):
            self.canv.setFont(font, size)
            self.canv.setFillColor(col)
            self.canv.drawString(tx, ty - i * (size + 2), text)


# ─── Helpers ──────────────────────────────────────────────────────────────────

def _style(name, **kw):
    """Create and return a named ParagraphStyle with the given attributes."""
    return ParagraphStyle(name, **kw)


def _priority_block(label, subtitle, items, accent_color, label_color, W):
    """Build and return a KeepTogether priority block with teal/grey accent bar."""
    block = []

    hdr_data = [[
        Paragraph(label,    _style("ph", fontName="Helvetica-Bold",
                                   fontSize=8.5, textColor=WHITE, leading=12)),
        Paragraph(subtitle, _style("ps", fontName="Helvetica",
                                   fontSize=8, textColor=colors.HexColor("#CCCCCC"),
                                   leading=12, alignment=TA_RIGHT)),
    ]]
    hdr = Table(hdr_data, colWidths=[W * 0.45, W * 0.55])
    hdr.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), accent_color),
        ("LEFTPADDING",   (0, 0), (0, 0),   4*mm),
        ("RIGHTPADDING",  (1, 0), (1, 0),   4*mm),
        ("TOPPADDING",    (0, 0), (-1, -1), 2.5*mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5*mm),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    block.append(hdr)

    for item in items:
        block.append(Paragraph(
            f"<bullet>&bull;</bullet> {item}",
            _style("bi", fontName="Helvetica", fontSize=9, textColor=GREY_BODY,
                   leading=14, leftIndent=10*mm, firstLineIndent=-6*mm,
                   spaceBefore=2*mm),
        ))
    block.append(Spacer(1, 5*mm))
    return KeepTogether(block)


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
        leftMargin=20*mm,
        rightMargin=20*mm,
        topMargin=10*mm,
        bottomMargin=18*mm,
        title="Resume Match Score Report",
        author=REVIEWER_NAME,
        subject=f"Resume score for {data.get('candidate_name', 'Candidate')}",
        creator=f"{REVIEWER_NAME} via Job Search AI Kit",
        producer="Job Search AI Kit",
        encrypt=StandardEncryption(
            "", canPrint=1, canModify=0, canCopy=0, canAnnotate=0
        ),
    )

    W = A4[0] - 40*mm   # usable width
    story = []

    # ── TOP TEAL ACCENT BAR ───────────────────────────────────────────────────
    story.append(TealBar(W, height=4))
    story.append(Spacer(1, 5*mm))

    # ── DOCUMENT META LABEL ───────────────────────────────────────────────────
    story.append(Paragraph(
        "RESUME MATCH SCORE REPORT",
        _style("meta", fontName="Helvetica", fontSize=7.5,
               textColor=TEAL, leading=10, letterSpacing=1.8),
    ))
    story.append(Spacer(1, 3*mm))

    # ── ROLE + COMPANY HEADLINE ───────────────────────────────────────────────
    story.append(Paragraph(
        data.get("role_title", "Role"),
        _style("h1", fontName="Helvetica-Bold", fontSize=22,
               textColor=INK, leading=26),
    ))
    story.append(Spacer(1, 1*mm))
    story.append(Paragraph(
        f"{data.get('company', '')}  &nbsp;&nbsp;·&nbsp;&nbsp;  {date_str}",
        _style("co", fontName="Helvetica", fontSize=10,
               textColor=GREY_LABEL, leading=14),
    ))
    story.append(Spacer(1, 4*mm))

    # ── REVIEWER STAMP (small, right-side) ───────────────────────────────────
    reviewer_lines = [
        (f"Reviewed by  {REVIEWER_NAME}", "Helvetica-Bold", 8.5, INK),
        (REVIEWER_TITLE,                  "Helvetica",      7.5, GREY_LABEL),
    ]
    reviewer_stamp = ReviewerStamp(PHOTO_PATH, diameter=13*mm,
                                   text_lines=reviewer_lines)
    story.append(reviewer_stamp)
    story.append(Spacer(1, 3*mm))

    # ── DIVIDER ───────────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=0.75, color=RULE,
                             spaceAfter=5*mm))

    # ── CANDIDATE INFO + CONTACT LINKS ───────────────────────────────────────
    cname   = data.get("candidate_name", "")
    c_email = data.get("candidate_email", "")
    c_phone = data.get("candidate_phone", "")
    c_li    = data.get("candidate_linkedin", "")
    c_gh    = data.get("candidate_github", "")

    S_LINK = _style("lnk", fontName="Helvetica", fontSize=8.5,
                    textColor=TEAL, leading=12)
    S_CAND = _style("cnd", fontName="Helvetica-Bold", fontSize=10,
                    textColor=INK, leading=14)

    if cname:
        story.append(Paragraph(cname, S_CAND))
        story.append(Spacer(1, 1.5*mm))

    contact_parts = []
    if c_email:
        contact_parts.append(f'<link href="mailto:{c_email}">{c_email}</link>')
    if c_phone:
        tel_uri = re.sub(r"[\s\-()]", "", c_phone)
        contact_parts.append(f'<link href="tel:{tel_uri}">{c_phone}</link>')
    if c_li:
        contact_parts.append(f'<link href="{c_li}">LinkedIn Profile</link>')
    if c_gh:
        contact_parts.append(f'<link href="{c_gh}">GitHub Portfolio</link>')
    if contact_parts:
        story.append(Paragraph("  ·  ".join(contact_parts), S_LINK))
        story.append(Spacer(1, 6*mm))

    # ── SCORE BREAKDOWN ───────────────────────────────────────────────────────
    story.append(Paragraph(
        "SCORE BREAKDOWN",
        _style("sec", fontName="Helvetica-Bold", fontSize=7.5,
               textColor=TEAL, leading=10, letterSpacing=1.5,
               spaceBefore=2*mm, spaceAfter=2*mm),
    ))

    dimension_labels = {
        "keyword_match":    "Keyword Match",
        "skills_alignment": "Skills Alignment",
        "experience":       "Experience Relevance",
        "achievements":     "Achievement Quality",
        "structure_ats":    "Structure & ATS Safety",
        "education":        "Education & Credentials",
    }

    bar_col_w = W * 0.50
    rows = []
    for key, label in dimension_labels.items():
        entry = data["scores"].get(key, {"score": 0, "max": 0})
        sc, mx = entry["score"], entry["max"]
        rows.append([
            Paragraph(label, _style("sl", fontName="Helvetica", fontSize=9,
                                    textColor=GREY_BODY, leading=12)),
            ScoreBar(sc, mx, width=bar_col_w, height=6),
            Paragraph(f"<b>{sc}</b> / {mx}",
                      _style("sn", fontName="Helvetica", fontSize=9,
                             textColor=INK, leading=12, alignment=TA_RIGHT)),
        ])

    score_table = Table(
        rows,
        colWidths=[48*mm, bar_col_w, 22*mm],
        rowHeights=[8.5*mm] * len(rows),
    )
    score_table.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 0), (-1, -1), [WHITE, BAND_BG]),
        ("LEFTPADDING",   (0, 0), (-1, -1), 3*mm),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 3*mm),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LINEBELOW",     (0, -1), (-1, -1), 0.5, RULE),
    ]))
    story.append(score_table)
    story.append(Spacer(1, 5*mm))

    # ── TOTAL SCORE + RATING (clean two-column band) ──────────────────────────
    total  = data.get("total", sum(v["score"] for v in data["scores"].values()))
    rating = data.get("rating", "Competitive")
    r_col  = RATING_COLOURS.get(rating, TEAL)

    total_table = Table(
        [[
            Paragraph(
                f"<b>{total}</b> / 100",
                _style("tot", fontName="Helvetica-Bold", fontSize=28,
                       textColor=WHITE, leading=32),
            ),
            Paragraph(
                f"<b>{rating}</b>",
                _style("rat", fontName="Helvetica-Bold", fontSize=18,
                       textColor=r_col, leading=22, alignment=TA_RIGHT),
            ),
        ]],
        colWidths=[W * 0.4, W * 0.6],
    )
    total_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), INK),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING",   (0, 0), (0, 0),   5*mm),
        ("RIGHTPADDING",  (1, 0), (1, 0),   5*mm),
        ("TOPPADDING",    (0, 0), (-1, -1), 4*mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4*mm),
    ]))
    story.append(total_table)
    story.append(Spacer(1, 7*mm))

    # ── DIMENSION NOTES ───────────────────────────────────────────────────────
    notes = data.get("dimension_notes", {})
    note_rows = [
        (k, notes[k]) for k in dimension_labels if notes.get(k)
    ]
    if note_rows:
        story.append(Paragraph(
            "DIMENSION NOTES",
            _style("sec2", fontName="Helvetica-Bold", fontSize=7.5,
                   textColor=TEAL, leading=10, letterSpacing=1.5,
                   spaceAfter=2*mm),
        ))
        nt_data = [
            [
                Paragraph(dimension_labels[k],
                          _style("nl", fontName="Helvetica-Bold", fontSize=8.5,
                                 textColor=INK, leading=12)),
                Paragraph(v,
                          _style("nv", fontName="Helvetica-Oblique", fontSize=8.5,
                                 textColor=GREY_NOTE, leading=13)),
            ]
            for k, v in note_rows
        ]
        nt = Table(nt_data, colWidths=[52*mm, W - 52*mm])
        nt.setStyle(TableStyle([
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("ROWBACKGROUNDS",(0, 0), (-1, -1), [WHITE, BAND_BG]),
            ("LEFTPADDING",   (0, 0), (-1, -1), 3*mm),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 3*mm),
            ("TOPPADDING",    (0, 0), (-1, -1), 2.5*mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5*mm),
        ]))
        story.append(nt)
        story.append(Spacer(1, 7*mm))

    # ── ACTION PLAN ───────────────────────────────────────────────────────────
    story.append(Paragraph(
        "ACTION PLAN",
        _style("sec3", fontName="Helvetica-Bold", fontSize=7.5,
               textColor=TEAL, leading=10, letterSpacing=1.5,
               spaceAfter=2*mm),
    ))

    priorities = [
        ("priority_1", "PRIORITY 1", "Do this before applying",
         colors.HexColor("#1C1C1C"), TEAL),
        ("priority_2", "PRIORITY 2", "Strongly recommended",
         colors.HexColor("#3A3A3A"), colors.HexColor("#AAAAAA")),
        ("priority_3", "PRIORITY 3", "Nice to have",
         colors.HexColor("#555555"), colors.HexColor("#AAAAAA")),
    ]

    for key, label, subtitle, accent, _ in priorities:
        items = data.get(key, [])
        if items:
            story.append(_priority_block(label, subtitle, items, accent, TEAL, W))

    # ── FOOTER ────────────────────────────────────────────────────────────────
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.75, color=RULE,
                             spaceAfter=3*mm))

    footer_table = Table(
        [[
            Paragraph(
                f"<b>{REVIEWER_NAME}</b>  ·  {REVIEWER_TITLE}",
                _style("fl", fontName="Helvetica", fontSize=7.5,
                       textColor=GREY_LABEL, leading=11),
            ),
            Paragraph(
                f'<link href="{SERIES_URL}"><font color="#16B2B2">'
                f'Follow the series: {REVIEWER_BRAND}</font></link>',
                _style("fr", fontName="Helvetica", fontSize=7.5,
                       textColor=GREY_LABEL, leading=11, alignment=TA_RIGHT),
            ),
        ]],
        colWidths=[W * 0.5, W * 0.5],
    )
    footer_table.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(footer_table)

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

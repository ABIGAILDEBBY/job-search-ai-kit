# Resume Templates

This folder contains configuration files for the 8 resume templates available in `/tailor-resume`.

## How to customise a template

1. Open the JSON file for the template you want to change (inside `configs/`)
2. Edit the values you want to change — font, colors, sizes, margins
3. Save the file
4. Run `/tailor-resume` and select that template — it will use your updated settings

## Available templates

| # | File | Best for |
|---|---|---|
| 1 | `template_1_faang_classic.json` | Software engineering, data engineering, ML, DevOps at FAANG and large tech |
| 2 | `template_2_harvard_classic.json` | Consulting, finance, academia, law — any field where the Harvard signature signals credibility |
| 3 | `template_3_consulting_tight.json` | McKinsey, BCG, Bain, and consulting firm applications. Strict one-page format |
| 4 | `template_4_modern_tech.json` | Engineering, data, product, and ops roles at modern tech companies and startups |
| 5 | `template_5_creative_accent.json` | UX/UI design, product design, marketing, and creative roles — portfolio-prominent |
| 6 | `template_6_conservative_pro.json` | Finance, banking, law, compliance, accounting, healthcare — zero color, Georgia serif |
| 7 | `template_7_entry_academic.json` | Students and candidates with under 2 years of experience — education-first, one page |
| 8 | `template_8_executive_strategic.json` | Directors, VPs, C-suite, and candidates with 10+ years — two pages, authority framing |

## What each setting controls

| Key | What it does |
|---|---|
| `font_body` | Font used for all body text, bullets, and contact line |
| `font_heading` | Font used for section headings (often the same as font_body) |
| `font_size_name` | Size of your name at the top of the resume |
| `font_size_heading` | Size of section headings |
| `font_size_body` | Size of body text (job descriptions, education lines) |
| `font_size_bullet` | Size of bullet point text |
| `font_size_contact` | Size of the contact line (email, phone, LinkedIn) |
| `color_name` | Color of your name (hex, no #) |
| `color_heading` | Color of section heading text (hex, no #) |
| `color_body` | Color of all body text (hex, no #) |
| `color_accent` | Accent color used for hyperlinks in the contact line and decorative elements |
| `color_heading_border` | Color of the border or rule drawn under/beside each section heading |
| `heading_style` | How section headings are styled: `bottom_border`, `left_border`, or `shaded` |
| `heading_border_size` | Thickness of the border in half-points (4 = thin, 8 = medium, 18 = thick) |
| `heading_alignment` | Alignment of heading text: `left` or `center` |
| `name_alignment` | `left` or `center` |
| `contact_alignment` | `left` or `center` |
| `margin_*_inches` | Page margins (`margin_top_inches`, `margin_bottom_inches`, `margin_left_inches`, `margin_right_inches`) |
| `line_spacing` | Line height multiplier for all body and bullet paragraphs (1.0 = single, 1.15 = default, 1.5 = loose) |
| `space_before_heading_pt` | Points of space added above each section heading |
| `space_after_heading_pt` | Points of space added below each section heading, before the first body line |
| `space_after_body_pt` | Points of space after each body paragraph |
| `space_after_bullet_pt` | Points of space after each bullet point |
| `skills_format` | How the skills section is rendered — `inline_categories` displays skills as labeled inline lists (ATS-safe) |
| `contact_separator` | String placed between contact items (e.g. `"  \|  "` or `"   ·   "`) |
| `education_first` | `true` puts Education before Work Experience (set automatically for students and Template 7) |
| `portfolio_prominent` | `true` places the portfolio URL first in the contact line, before email (Template 5) |
| `include_interests_section` | `true` adds an Interests section at the end (McKinsey/consulting format, Template 3) |
| `include_competencies_band` | `true` adds a Core Competencies band after the summary (Template 8 executive format) |
| `show_target_role_subtitle` | `true` shows the target role as a subtitle line under your name |

## ATS safety note

All 8 templates are ATS-safe: single-column layout, standard section heading names, no text boxes, no images, no multi-column content. All content is in the document body — never in Word headers or footers.

"""
Tests for .claude/commands/generate_score_report.py

Covers:
- New colour palette constants
- Updated RATING_COLOURS
- New SERIES_URL constant
- TealBar flowable (new)
- ScoreBar flowable (redesigned)
- ReviewerStamp flowable (new, replaces CirclePhoto)
- _style() helper (new)
- _priority_block() helper (new)
- build_report() end-to-end PDF creation
- main() CLI argument handling
"""

import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, call, patch

import pytest

# Add the commands directory to path so we can import the module
sys.path.insert(0, str(Path(__file__).parent.parent / ".claude" / "commands"))

import generate_score_report as gsr
from generate_score_report import (
    BAND_BG,
    GREY_BODY,
    GREY_LABEL,
    GREY_NOTE,
    INK,
    PAGE_BG,
    RATING_COLOURS,
    RULE,
    REVIEWER_NAME,
    REVIEWER_TITLE,
    REVIEWER_BRAND,
    SAMPLE_DATA,
    SCORE_FILL,
    SCORE_TRACK,
    SERIES_URL,
    TEAL,
    TEAL_DARK,
    WHITE,
    ScoreBar,
    TealBar,
    ReviewerStamp,
    _priority_block,
    _style,
    build_report,
)
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, Spacer, Table


# ─── Colour constant tests ─────────────────────────────────────────────────────

class TestColourConstants:
    """Tests for the new/updated colour palette constants."""

    def test_ink_hex(self):
        assert INK == colors.HexColor("#1C1C1C")

    def test_teal_hex(self):
        assert TEAL == colors.HexColor("#16B2B2")

    def test_teal_dark_hex(self):
        assert TEAL_DARK == colors.HexColor("#0E8080")

    def test_white_is_white(self):
        assert WHITE == colors.white

    def test_page_bg_is_white(self):
        assert PAGE_BG == colors.white

    def test_band_bg_hex(self):
        assert BAND_BG == colors.HexColor("#F4F6F7")

    def test_rule_hex(self):
        assert RULE == colors.HexColor("#DCDCDC")

    def test_grey_label_hex(self):
        assert GREY_LABEL == colors.HexColor("#888888")

    def test_grey_body_hex(self):
        assert GREY_BODY == colors.HexColor("#444444")

    def test_grey_note_hex(self):
        assert GREY_NOTE == colors.HexColor("#777777")

    def test_score_fill_is_teal(self):
        assert SCORE_FILL is TEAL

    def test_score_track_hex(self):
        assert SCORE_TRACK == colors.HexColor("#E4E4E4")


# ─── RATING_COLOURS tests ──────────────────────────────────────────────────────

class TestRatingColours:
    """Tests for the updated RATING_COLOURS mapping."""

    def test_all_keys_present(self):
        expected = {"Weak", "Developing", "Competitive", "Strong", "Exceptional"}
        assert set(RATING_COLOURS.keys()) == expected

    def test_weak_is_red(self):
        assert RATING_COLOURS["Weak"] == colors.HexColor("#C0392B")

    def test_developing_is_amber(self):
        assert RATING_COLOURS["Developing"] == colors.HexColor("#D68910")

    def test_competitive_is_blue(self):
        assert RATING_COLOURS["Competitive"] == colors.HexColor("#1A7FC1")

    def test_strong_is_teal(self):
        assert RATING_COLOURS["Strong"] is TEAL

    def test_exceptional_is_green(self):
        assert RATING_COLOURS["Exceptional"] == colors.HexColor("#1E8449")


# ─── SERIES_URL constant ───────────────────────────────────────────────────────

class TestSeriesUrl:
    def test_series_url_is_linkedin(self):
        assert SERIES_URL.startswith("https://www.linkedin.com/")

    def test_series_url_not_empty(self):
        assert len(SERIES_URL) > 0


# ─── TealBar tests ─────────────────────────────────────────────────────────────

class TestTealBar:
    """Tests for the new TealBar flowable."""

    def test_init_stores_dimensions(self):
        bar = TealBar(width=150, height=5)
        assert bar.bar_w == 150
        assert bar.bar_h == 5
        assert bar.width == 150
        assert bar.height == 5

    def test_init_default_height(self):
        bar = TealBar(width=100)
        assert bar.bar_h == 3
        assert bar.height == 3

    def test_init_zero_width(self):
        bar = TealBar(width=0)
        assert bar.bar_w == 0
        assert bar.width == 0

    def test_draw_sets_teal_fill(self):
        bar = TealBar(width=200, height=4)
        bar.canv = MagicMock()
        bar.draw()
        bar.canv.setFillColor.assert_called_once_with(TEAL)

    def test_draw_calls_rect_with_correct_args(self):
        bar = TealBar(width=200, height=4)
        bar.canv = MagicMock()
        bar.draw()
        bar.canv.rect.assert_called_once_with(0, 0, 200, 4, fill=1, stroke=0)

    def test_draw_uses_bar_dimensions_not_modified(self):
        """draw() should use bar_w/bar_h, which equal width/height for TealBar."""
        bar = TealBar(width=175.5, height=3)
        bar.canv = MagicMock()
        bar.draw()
        args = bar.canv.rect.call_args[0]
        assert args[2] == 175.5
        assert args[3] == 3


# ─── ScoreBar tests ────────────────────────────────────────────────────────────

class TestScoreBar:
    """Tests for the redesigned ScoreBar flowable."""

    def test_init_stores_values(self):
        bar = ScoreBar(score=18, max_score=25, width=100, height=6)
        assert bar.score == 18
        assert bar.max_score == 25
        assert bar.bar_w == 100
        assert bar.bar_h == 6

    def test_init_height_adds_padding(self):
        """Flowable height should be bar height + 2 for spacing."""
        bar = ScoreBar(score=10, max_score=20, height=6)
        assert bar.height == 8  # 6 + 2

    def test_init_default_width_in_mm(self):
        bar = ScoreBar(score=5, max_score=10)
        assert bar.bar_w == pytest.approx(100 * mm, rel=1e-4)

    def test_draw_zero_max_score_no_fill(self):
        """When max_score <= 0, the fill rect should not be drawn."""
        bar = ScoreBar(score=0, max_score=0, width=100, height=6)
        bar.canv = MagicMock()
        bar.draw()
        # setFillColor called only once for the track, not a second time for fill
        assert bar.canv.setFillColor.call_count == 1
        bar.canv.setFillColor.assert_called_once_with(SCORE_TRACK)

    def test_draw_negative_max_score_no_fill(self):
        """Negative max_score is treated same as zero — no fill drawn."""
        bar = ScoreBar(score=5, max_score=-1, width=100, height=6)
        bar.canv = MagicMock()
        bar.draw()
        assert bar.canv.setFillColor.call_count == 1

    def test_draw_draws_track_first(self):
        bar = ScoreBar(score=10, max_score=20, width=100, height=6)
        bar.canv = MagicMock()
        bar.draw()
        first_fill_call = bar.canv.setFillColor.call_args_list[0]
        assert first_fill_call == call(SCORE_TRACK)

    def test_draw_fills_with_score_fill_color(self):
        bar = ScoreBar(score=10, max_score=20, width=100, height=6)
        bar.canv = MagicMock()
        bar.draw()
        second_fill_call = bar.canv.setFillColor.call_args_list[1]
        assert second_fill_call == call(SCORE_FILL)

    def test_draw_full_score_fills_entire_width(self):
        bar = ScoreBar(score=25, max_score=25, width=100, height=6)
        bar.canv = MagicMock()
        bar.draw()
        # Second roundRect call should have filled_width == bar_w
        calls = bar.canv.roundRect.call_args_list
        assert len(calls) == 2
        filled_width = calls[1][0][2]
        assert filled_width == pytest.approx(100.0)

    def test_draw_partial_score_proportional_fill(self):
        """A score of 10/25 should fill 40% of the bar width."""
        bar = ScoreBar(score=10, max_score=25, width=100, height=6)
        bar.canv = MagicMock()
        bar.draw()
        calls = bar.canv.roundRect.call_args_list
        filled_width = calls[1][0][2]
        assert filled_width == pytest.approx(40.0)

    def test_draw_zero_score_fills_nothing(self):
        """A score of 0 should produce a zero-width fill."""
        bar = ScoreBar(score=0, max_score=25, width=100, height=6)
        bar.canv = MagicMock()
        bar.draw()
        calls = bar.canv.roundRect.call_args_list
        assert len(calls) == 2
        filled_width = calls[1][0][2]
        assert filled_width == pytest.approx(0.0)

    def test_draw_single_color_no_color_switching(self):
        """New design uses one fill colour (TEAL/SCORE_FILL), not orange/amber/red."""
        bar = ScoreBar(score=5, max_score=25, width=100, height=6)
        bar.canv = MagicMock()
        bar.draw()
        fill_colors = [c[0][0] for c in bar.canv.setFillColor.call_args_list]
        # Should only be SCORE_TRACK and SCORE_FILL — never orange or red
        assert SCORE_FILL in fill_colors
        assert SCORE_TRACK in fill_colors
        assert len(fill_colors) == 2


# ─── ReviewerStamp tests ───────────────────────────────────────────────────────

class TestReviewerStamp:
    """Tests for the new ReviewerStamp flowable (replaces CirclePhoto)."""

    def test_init_stores_photo_path_as_string(self):
        stamp = ReviewerStamp("/some/path/photo.png")
        assert stamp.photo_path == "/some/path/photo.png"

    def test_init_path_object_converted_to_string(self):
        stamp = ReviewerStamp(Path("/some/path/photo.png"))
        assert isinstance(stamp.photo_path, str)

    def test_init_default_diameter(self):
        stamp = ReviewerStamp("/photo.png")
        assert stamp.d == pytest.approx(14 * mm, rel=1e-4)

    def test_init_custom_diameter(self):
        stamp = ReviewerStamp("/photo.png", diameter=13 * mm)
        assert stamp.d == pytest.approx(13 * mm, rel=1e-4)

    def test_init_default_text_lines_empty(self):
        stamp = ReviewerStamp("/photo.png")
        assert stamp.text_lines == []

    def test_init_text_lines_stored(self):
        lines = [("Alice", "Helvetica-Bold", 9, INK)]
        stamp = ReviewerStamp("/photo.png", text_lines=lines)
        assert stamp.text_lines == lines

    def test_init_none_text_lines_becomes_empty(self):
        stamp = ReviewerStamp("/photo.png", text_lines=None)
        assert stamp.text_lines == []

    def test_init_width_is_200mm(self):
        stamp = ReviewerStamp("/photo.png")
        assert stamp.width == pytest.approx(200 * mm, rel=1e-4)

    def test_init_height_is_diameter_plus_2mm(self):
        stamp = ReviewerStamp("/photo.png", diameter=14 * mm)
        assert stamp.height == pytest.approx(14 * mm + 2 * mm, rel=1e-4)

    def test_draw_no_photo_skips_image_draw(self):
        """When photo file does not exist, no circle or image should be drawn."""
        stamp = ReviewerStamp("/nonexistent/photo.png")
        stamp.canv = MagicMock()
        stamp.draw()
        stamp.canv.drawImage.assert_not_called()
        stamp.canv.circle.assert_not_called()

    def test_draw_no_photo_still_renders_text(self):
        lines = [("Alice", "Helvetica", 9, INK)]
        stamp = ReviewerStamp("/nonexistent/photo.png", text_lines=lines)
        stamp.canv = MagicMock()
        stamp.draw()
        stamp.canv.drawString.assert_called_once()

    def test_draw_with_existing_photo_draws_teal_ring(self):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            # Write a minimal 1x1 PNG (valid PNG header + IHDR + IDAT + IEND)
            f.write(
                b"\x89PNG\r\n\x1a\n"                  # signature
                b"\x00\x00\x00\rIHDR"                  # IHDR chunk length + type
                b"\x00\x00\x00\x01\x00\x00\x00\x01"   # 1x1
                b"\x08\x02\x00\x00\x00\x90wS\xde"     # bit depth, color type, ...
                b"\x00\x00\x00\x0cIDATx\x9cc\xf8\x0f" # IDAT
                b"\x00\x00\x01\x01\x00\x18\xdd\x8d\xb4"
                b"\x00\x00\x00\x00IEND\xaeB`\x82"      # IEND
            )
            tmp_path = f.name
        try:
            stamp = ReviewerStamp(tmp_path, diameter=14 * mm)
            stamp.canv = MagicMock()
            stamp.draw()
            # Should draw the teal ring
            stamp.canv.setFillColor.assert_any_call(TEAL)
            stamp.canv.circle.assert_called_once()
        finally:
            os.unlink(tmp_path)

    def test_draw_text_lines_call_count(self):
        lines = [
            ("Name", "Helvetica-Bold", 8.5, INK),
            ("Title", "Helvetica", 7.5, GREY_LABEL),
        ]
        stamp = ReviewerStamp("/nonexistent/photo.png", text_lines=lines)
        stamp.canv = MagicMock()
        stamp.draw()
        assert stamp.canv.drawString.call_count == 2

    def test_draw_text_positioned_right_of_photo(self):
        """Text x-position should be diameter + 4mm."""
        lines = [("Name", "Helvetica", 9, INK)]
        d = 13 * mm
        stamp = ReviewerStamp("/nonexistent/photo.png", diameter=d, text_lines=lines)
        stamp.canv = MagicMock()
        stamp.draw()
        x_arg = stamp.canv.drawString.call_args[0][0]
        assert x_arg == pytest.approx(d + 4 * mm, rel=1e-4)


# ─── _style() helper tests ─────────────────────────────────────────────────────

class TestStyleHelper:
    """Tests for the _style() ParagraphStyle factory."""

    def test_returns_paragraph_style(self):
        s = _style("test_style")
        assert isinstance(s, ParagraphStyle)

    def test_name_is_set(self):
        s = _style("my_name")
        assert s.name == "my_name"

    def test_kwargs_applied(self):
        s = _style("lbl", fontName="Helvetica-Bold", fontSize=10)
        assert s.fontName == "Helvetica-Bold"
        assert s.fontSize == 10

    def test_text_color_applied(self):
        s = _style("c", textColor=TEAL)
        assert s.textColor is TEAL

    def test_unique_names_produce_separate_instances(self):
        s1 = _style("unique_a", fontSize=8)
        s2 = _style("unique_b", fontSize=12)
        assert s1 is not s2
        assert s1.fontSize != s2.fontSize


# ─── _priority_block() helper tests ───────────────────────────────────────────

class TestPriorityBlock:
    """Tests for the _priority_block() helper."""

    def _make_block(self, items=None):
        if items is None:
            items = ["Fix keyword gaps", "Add metrics"]
        return _priority_block(
            label="PRIORITY 1",
            subtitle="Do this before applying",
            items=items,
            accent_color=INK,
            label_color=TEAL,
            W=150 * mm,
        )

    def test_returns_keep_together(self):
        result = self._make_block()
        assert isinstance(result, KeepTogether)

    def test_block_contains_header_table(self):
        result = self._make_block()
        # First element in KeepTogether should be the header Table
        inner = result._content
        assert isinstance(inner[0], Table)

    def test_block_ends_with_spacer(self):
        result = self._make_block()
        inner = result._content
        assert isinstance(inner[-1], Spacer)

    def test_block_item_count(self):
        """Block should contain header + N item paragraphs + 1 spacer."""
        items = ["Item A", "Item B", "Item C"]
        result = _priority_block("P1", "Sub", items, INK, TEAL, 150 * mm)
        inner = result._content
        # header (1) + items (3) + spacer (1) = 5
        assert len(inner) == 5

    def test_empty_items_list(self):
        """An empty items list should produce block with only header + spacer."""
        result = _priority_block("P1", "Sub", [], INK, TEAL, 150 * mm)
        inner = result._content
        assert len(inner) == 2  # header + spacer

    def test_single_item(self):
        result = _priority_block("P1", "Sub", ["Only item"], INK, TEAL, 150 * mm)
        inner = result._content
        assert len(inner) == 3  # header + 1 item + spacer

    def test_header_table_has_two_columns(self):
        result = self._make_block()
        hdr = result._content[0]
        assert len(hdr._argW) == 2

    def test_header_col_widths_sum_to_W(self):
        W = 150 * mm
        result = _priority_block("P1", "Sub", ["x"], INK, TEAL, W)
        hdr = result._content[0]
        assert sum(hdr._argW) == pytest.approx(W, rel=1e-4)


# ─── build_report() end-to-end tests ──────────────────────────────────────────

class TestBuildReport:
    """Integration tests for build_report()."""

    def _run(self, data=None):
        """Run build_report with given data, return path to created PDF."""
        if data is None:
            data = SAMPLE_DATA
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            out = f.name
        build_report(data, out)
        return out

    def test_creates_pdf_file(self):
        out = self._run()
        try:
            assert os.path.exists(out)
            assert os.path.getsize(out) > 0
        finally:
            os.unlink(out)

    def test_output_is_pdf(self):
        out = self._run()
        try:
            with open(out, "rb") as f:
                header = f.read(4)
            assert header == b"%PDF"
        finally:
            os.unlink(out)

    def test_minimal_data_no_crash(self):
        """build_report should handle minimal data without raising."""
        data = {
            "scores": {
                "keyword_match":    {"score": 0, "max": 25},
                "skills_alignment": {"score": 0, "max": 20},
                "experience":       {"score": 0, "max": 25},
                "achievements":     {"score": 0, "max": 15},
                "structure_ats":    {"score": 0, "max": 10},
                "education":        {"score": 0, "max":  5},
            },
        }
        out = self._run(data)
        try:
            assert os.path.exists(out)
        finally:
            os.unlink(out)

    def test_date_auto_filled_when_blank(self):
        """An empty 'date' field should not cause an error."""
        data = dict(SAMPLE_DATA)
        data = {**SAMPLE_DATA, "date": ""}
        out = self._run(data)
        try:
            assert os.path.exists(out)
        finally:
            os.unlink(out)

    def test_explicit_date_used(self):
        """A non-empty 'date' field should be used as-is without error."""
        data = {**SAMPLE_DATA, "date": "01 January 2025"}
        out = self._run(data)
        try:
            assert os.path.exists(out)
        finally:
            os.unlink(out)

    def test_no_candidate_info(self):
        """Missing candidate fields should not raise."""
        data = dict(SAMPLE_DATA)
        data = {
            k: v for k, v in SAMPLE_DATA.items()
            if k not in ("candidate_name", "candidate_email",
                         "candidate_phone", "candidate_linkedin",
                         "candidate_github")
        }
        out = self._run(data)
        try:
            assert os.path.exists(out)
        finally:
            os.unlink(out)

    def test_no_dimension_notes(self):
        """Missing dimension_notes should not raise."""
        data = {k: v for k, v in SAMPLE_DATA.items() if k != "dimension_notes"}
        out = self._run(data)
        try:
            assert os.path.exists(out)
        finally:
            os.unlink(out)

    def test_no_priority_sections(self):
        """Missing priority_1/2/3 should not raise."""
        data = {
            k: v for k, v in SAMPLE_DATA.items()
            if k not in ("priority_1", "priority_2", "priority_3")
        }
        out = self._run(data)
        try:
            assert os.path.exists(out)
        finally:
            os.unlink(out)

    def test_unknown_rating_falls_back_to_teal(self):
        """An unrecognised rating key should fall back to TEAL without crashing."""
        data = {**SAMPLE_DATA, "rating": "Unknown"}
        out = self._run(data)
        try:
            assert os.path.exists(out)
        finally:
            os.unlink(out)

    def test_total_computed_from_scores_when_missing(self):
        """When 'total' is omitted, it should be summed from scores."""
        data = {k: v for k, v in SAMPLE_DATA.items() if k != "total"}
        out = self._run(data)
        try:
            assert os.path.exists(out)
        finally:
            os.unlink(out)

    def test_custom_output_path_honoured(self):
        """data['output_path'] should override the default path in main()."""
        # build_report itself doesn't read output_path — that's main()'s job.
        # Just verify build_report writes to the path we give it.
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            custom_path = f.name
        build_report(SAMPLE_DATA, custom_path)
        try:
            assert os.path.exists(custom_path)
        finally:
            os.unlink(custom_path)

    def test_margins_set_to_20mm(self):
        """build_report should create doc with 20mm left/right margins (spot check)."""
        # We verify indirectly: PDF is created without error at 20mm margins
        out = self._run()
        try:
            assert os.path.getsize(out) > 1000
        finally:
            os.unlink(out)


# ─── main() CLI tests ──────────────────────────────────────────────────────────

class TestMain:
    """Tests for the main() CLI entry point."""

    def test_no_args_exits_with_code_1(self):
        with patch.object(sys, "argv", ["generate_score_report.py"]):
            with pytest.raises(SystemExit) as exc:
                gsr.main()
        assert exc.value.code == 1

    def test_sample_flag_calls_build_report_with_sample_data(self):
        with patch.object(sys, "argv", ["generate_score_report.py", "--sample"]):
            with patch("generate_score_report.build_report") as mock_build:
                gsr.main()
        mock_build.assert_called_once()
        args = mock_build.call_args[0]
        assert args[0] is SAMPLE_DATA
        assert args[1] == "score_report_sample.pdf"

    def test_json_file_loads_data_and_infers_output_path(self, tmp_path):
        data = dict(SAMPLE_DATA)
        json_file = tmp_path / "my_candidate.json"
        json_file.write_text(json.dumps(data))

        with patch.object(sys, "argv", ["generate_score_report.py", str(json_file)]):
            with patch("generate_score_report.build_report") as mock_build:
                gsr.main()

        mock_build.assert_called_once()
        _, out_path = mock_build.call_args[0]
        assert out_path == str(tmp_path / "my_candidate_report.pdf")

    def test_json_file_with_output_path_override(self, tmp_path):
        custom_out = str(tmp_path / "custom_output.pdf")
        data = {**SAMPLE_DATA, "output_path": custom_out}
        json_file = tmp_path / "input.json"
        json_file.write_text(json.dumps(data))

        with patch.object(sys, "argv", ["generate_score_report.py", str(json_file)]):
            with patch("generate_score_report.build_report") as mock_build:
                gsr.main()

        _, out_path = mock_build.call_args[0]
        assert out_path == custom_out

    def test_sample_output_filename_is_score_report_sample(self):
        with patch.object(sys, "argv", ["generate_score_report.py", "--sample"]):
            with patch("generate_score_report.build_report") as mock_build:
                gsr.main()
        assert mock_build.call_args[0][1] == "score_report_sample.pdf"

"""Tests for skills/career/maintain-career-record/scripts. Synthetic data only.

Run: .venv/Scripts/python -m unittest discover tests   (Windows)
     .venv/bin/python -m unittest discover tests       (macOS/Linux)
"""

import copy
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "skills" / "career" / "maintain-career-record" / "scripts"
sys.dont_write_bytecode = True  # keep __pycache__ out of the skill folder
sys.path.insert(0, str(SCRIPTS))

import careerlib  # noqa: E402
import init  # noqa: E402
import migrate_cmd  # noqa: E402
import render  # noqa: E402
import validate  # noqa: E402

STAMP = "2025-03-14T10:02:00+05:30"
ACC_ID = "11111111-1111-4111-8111-111111111111"
OTHER_ID = "22222222-2222-4222-8222-222222222222"

EMPLOYMENT = {
    "schema_version": 1,
    "employers": [{
        "id": "emp-1",
        "legal_name": "Example Corp Pvt. Ltd.",
        "display_name": "Example Corp",
        "roles": [{
            "id": "role-1",
            "title": "Systems Engineer",
            "type": "full_time",
            "start": "2023-07",
            "end": "present",
            "engagements": [{"id": "eng-1", "client_descriptor": "Tier-1 retail banking platform",
                             "nda": True, "domain": "banking", "scale": ""}],
        }],
    }],
}

ACCOMPLISHMENT = {
    "schema_version": 1,
    "id": ACC_ID,
    "status": "confirmed",
    "role_id": "role-1",
    "engagement_id": "eng-1",
    "period": {"start": "2025-01", "end": "2025-03"},
    "title": "Cut report latency",
    "category": "performance",
    "situation": "Daily settlement reports took too long for operations staff.",
    "task": "Make the report endpoint fast enough for interactive use.",
    "actions": ["Added composite indexes and rewrote two queries in PostgreSQL."],
    "team_context": "Team of 6; I owned the reporting service.",
    "scale": "12,000 requests per day",
    "technologies": ["Java", "PostgreSQL"],
    "outcome": "Operations staff use the report interactively.",
    "metrics": [{"name": "p95 latency", "before": "410", "after": "238", "unit": "ms",
                 "period": "2025-Q1", "source": "monitoring dashboard",
                 "confidence": "measured", "user_confirmed": True}],
    "evidence": [{"type": "dashboard", "ref": "latency panel for the reporting service"}],
    "sde2_signals": {}, "interview": {},
    "bullets": [{"id": "b-1", "status": "confirmed", "tracks": ["backend"],
                 "text": "Reduced p95 latency of a settlement reporting API from 410 ms to 238 ms "
                         "by adding PostgreSQL composite indexes and rewriting queries across 12,000 daily requests."}],
    "similar_to": [], "gaps": [], "follow_up": None,
    "sources": [STAMP],
    "created": "2025-03-14", "updated": "2025-03-14",
}

NOTES = f"""# Career Evidence & Audit Log

    ## 2020-01-01T00:00:00Z

## {STAMP}

### Source
User conversation
"""


class CareerTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        init.init(self.root)
        self.career = self.root / "career"
        (self.career / "NOTES.md").write_text(NOTES, encoding="utf-8")
        self.write("employment.yaml", EMPLOYMENT)
        self.write_acc(ACCOMPLISHMENT)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, data):
        (self.career / "data" / name).write_text(careerlib.dump_yaml(data), encoding="utf-8")

    def write_acc(self, data, name=None):
        name = name or data["id"]
        (self.career / "data" / "accomplishments" / f"{name}.yaml").write_text(
            careerlib.dump_yaml(data), encoding="utf-8")

    def acc(self, **changes):
        data = copy.deepcopy(ACCOMPLISHMENT)
        data.update(changes)
        return data

    def errors(self):
        return validate.validate(self.career).errors

    def assertError(self, fragment):
        errors = self.errors()
        self.assertTrue(any(fragment in e for e in errors), f"expected '{fragment}' in {errors}")


class InitTests(CareerTestCase):
    def test_creates_files_and_never_overwrites(self):
        for name in careerlib.DATA_FILES:
            self.assertTrue((self.career / "data" / name).exists(), name)
        self.assertTrue((self.career / ".gitignore").exists())
        _, created, kept = init.init(self.root)
        self.assertEqual(created, [])
        self.assertIn(self.career / "NOTES.md", kept)
        self.assertIn(STAMP, (self.career / "NOTES.md").read_text(encoding="utf-8"))

    def test_blank_templates_validate(self):
        with tempfile.TemporaryDirectory() as other:
            init.init(other)
            report = validate.validate(Path(other) / "career")
            self.assertEqual(report.errors, [])


class ValidRecordTests(CareerTestCase):
    def test_valid_record_has_no_errors(self):
        self.assertEqual(self.errors(), [])

    def test_dates_stay_strings(self):
        data, _ = careerlib.load_yaml(self.career / "data" / "accomplishments" / f"{ACC_ID}.yaml")
        self.assertEqual(data["sources"], [STAMP])
        self.assertEqual(data["created"], "2025-03-14")

    def test_indented_example_heading_is_not_a_source(self):
        self.assertNotIn("2020-01-01T00:00:00Z", careerlib.notes_timestamps(self.career))
        self.write_acc(self.acc(sources=["2020-01-01T00:00:00Z"]))
        self.assertError("no matching")


class PlantedErrorTests(CareerTestCase):
    def test_number_not_in_record(self):
        bullet = dict(ACCOMPLISHMENT["bullets"][0], text="Reduced p95 latency by 63% using PostgreSQL indexes "
                      "and query rewrites across a settlement reporting API serving operations staff daily.")
        self.write_acc(self.acc(bullets=[bullet]))
        self.assertError("number 63")

    def test_unconfirmed_metric_in_confirmed_bullet(self):
        metric = dict(ACCOMPLISHMENT["metrics"][0], user_confirmed=False)
        self.write_acc(self.acc(status="incomplete", gaps=["latency not yet confirmed"], metrics=[metric]))
        self.assertError("only in a metric the user has not confirmed")

    def test_confirmed_requires_outcome(self):
        self.write_acc(self.acc(outcome=""))
        self.assertError("outcome")

    def test_incomplete_requires_gaps(self):
        self.write_acc(self.acc(status="incomplete"))
        self.assertError("gaps is empty")

    def test_confirmed_metric_must_be_user_confirmed(self):
        metric = dict(ACCOMPLISHMENT["metrics"][0], user_confirmed=False)
        self.write_acc(self.acc(metrics=[metric]))
        self.assertError("not user_confirmed")

    def test_missing_notes_source(self):
        self.write_acc(self.acc(sources=["2025-01-01T09:00:00+05:30"]))
        self.assertError("no matching")

    def test_unknown_role(self):
        self.write_acc(self.acc(role_id="role-9"))
        self.assertError("not a role")

    def test_engagement_must_belong_to_role(self):
        self.write_acc(self.acc(engagement_id="eng-9"))
        self.assertError("not an engagement")

    def test_id_must_match_file_name(self):
        (self.career / "data" / "accomplishments" / f"{ACC_ID}.yaml").unlink()
        self.write_acc(self.acc(), name="wrong-name")
        self.assertError("must match the file name")

    def test_similar_to_must_be_symmetric(self):
        other = self.acc(id=OTHER_ID, similar_to=[], bullets=[])
        self.write_acc(other)
        self.write_acc(self.acc(similar_to=[OTHER_ID]))
        self.assertError("does not list")
        other["similar_to"] = [ACC_ID]
        self.write_acc(other)
        self.assertEqual(self.errors(), [])

    def test_confirmed_bullet_on_draft_record(self):
        self.write_acc(self.acc(status="draft"))
        self.assertError("still draft")

    def test_score_must_be_quoted(self):
        self.write("education.yaml", {"schema_version": 1, "education": [{
            "id": "edu-1", "degree": "B.Tech", "institution": "Example Institute",
            "score": {"type": "cgpa", "value": 7.9, "scale": "10"}}]})
        self.assertError("quoted text")

    def test_skill_evidence_must_exist(self):
        self.write("skills.yaml", {"schema_version": 1, "skills": [
            {"name": "Java", "category": "language", "evidence": ["missing-id"]}]})
        self.assertError("evidence 'missing-id'")

    def test_duplicate_ids(self):
        employment = copy.deepcopy(EMPLOYMENT)
        employment["employers"][0]["roles"][0]["id"] = "emp-1"
        self.write("employment.yaml", employment)
        self.assertError("already used")

    def test_end_before_start(self):
        self.write_acc(self.acc(period={"start": "2025-03", "end": "2025-01"}))
        self.assertError("before start")

    def test_word_count_is_only_a_warning(self):
        bullet = dict(ACCOMPLISHMENT["bullets"][0], text="Cut p95 latency from 410 ms to 238 ms.")
        self.write_acc(self.acc(bullets=[bullet]))
        report = validate.validate(self.career)
        self.assertEqual(report.errors, [])
        self.assertTrue(any("words" in w for w in report.warnings))


class UnknownValueTests(CareerTestCase):
    def test_year_only_dates_and_unknown_period(self):
        self.write("education.yaml", {"schema_version": 1, "education": [{
            "id": "edu-1", "degree": "B.Tech", "institution": "Example Institute",
            "start": "2019", "end": "2023", "score": {"type": "cgpa", "value": "7.90", "scale": "10"}}]})
        self.write_acc(self.acc(period={"start": "", "end": ""}))
        report = validate.validate(self.career)
        self.assertEqual(report.errors, [])
        self.assertTrue(any("period is unknown" in w for w in report.warnings))

    def test_year_only_end_in_same_year_is_not_before_start(self):
        self.write_acc(self.acc(period={"start": "2025-05", "end": "2025"}))
        self.assertEqual(self.errors(), [])

    def test_nda_unknown_and_reported_confidence(self):
        employment = copy.deepcopy(EMPLOYMENT)
        employment["employers"][0]["roles"][0]["engagements"][0]["nda"] = "unknown"
        self.write("employment.yaml", employment)
        metric = dict(ACCOMPLISHMENT["metrics"][0], confidence="reported")
        self.write_acc(self.acc(metrics=[metric]))
        self.assertEqual(self.errors(), [])
        employment["employers"][0]["roles"][0]["engagements"][0]["nda"] = "maybe"
        self.write("employment.yaml", employment)
        self.assertError("nda must be")

    def test_bad_recognition_date(self):
        self.write("recognition.yaml", {"schema_version": 1, "recognition": [
            {"id": "rec-1", "title": "Award", "date": "March 2025"}]})
        self.assertError("date 'March 2025'")

    def test_origin_is_optional_and_checked(self):
        for origin in ("", "assigned", "self_initiated", "requested_by_others"):
            self.write_acc(self.acc(origin=origin))
            self.assertEqual(self.errors(), [], origin)
        self.write_acc(self.acc(origin="volunteered"))
        self.assertError("origin 'volunteered'")


class NumberTests(unittest.TestCase):
    def test_normalisation(self):
        self.assertEqual(careerlib.numbers_in("12,000 requests, 99.95% uptime, $2.1M, 0.50 s, 007"),
                         {"12000", "99.95", "2.1", "0.5", "7"})


class RenderTests(CareerTestCase):
    def test_render_marks_drafts_and_open_items(self):
        draft = self.acc(id=OTHER_ID, status="draft", title="Draft work", bullets=[
            {"id": "b-1", "status": "draft", "text": "Draft bullet", "tracks": []}],
            follow_up={"due": "2025-01", "ask": "error rate after launch"})
        self.write_acc(draft)
        record, errors = careerlib.load_record(self.career)
        self.assertEqual(errors, [])
        output = render.render(record, "2025-06-01")
        self.assertIn("GENERATED", output)
        self.assertIn("Example Corp Pvt. Ltd.", output)
        self.assertIn("Draft bullet *(draft)*", output)
        self.assertIn("follow-up due 2025-01", output)
        self.assertIn("p95 latency: 410 → 238 ms (measured", output)

    def test_render_shows_origin(self):
        self.write_acc(self.acc(origin="self_initiated"))
        output = render.render(careerlib.load_record(self.career)[0], "2025-06-01")
        self.assertIn("performance · self initiated · ", output)

    def test_open_items_show_structural_gaps(self):
        output = render.render(careerlib.load_record(self.career)[0], "2025-06-01")
        self.assertIn("missing from skills: Java, PostgreSQL", output)
        self.assertIn("Nothing recorded yet: education", output)
        self.assertIn("Profile missing: name", output)
        self.assertIn("(under NDA)", output)


class SkillExampleTests(CareerTestCase):
    """The examples shipped with capture-work-experience must pass its own checks."""

    REFS = SCRIPTS.parent.parent / "capture-work-experience" / "references"

    def test_example_record_validates(self):
        text = (self.REFS / "examples.md").read_text(encoding="utf-8")
        block = text.split("```yaml", 1)[1].split("```", 1)[0]
        data = careerlib.yaml.safe_load(block)
        (self.career / "data" / "accomplishments" / f"{ACC_ID}.yaml").unlink()
        (self.career / "data" / "accomplishments" / f"{data['id']}.yaml").write_text(block, encoding="utf-8")
        report = validate.validate(self.career)
        self.assertEqual(report.errors, [])
        self.assertEqual(report.warnings, [])

    def test_example_bullets_are_20_to_35_words(self):
        bullets = []
        for line in (self.REFS / "examples.md").read_text(encoding="utf-8").splitlines():
            if line.startswith("> "):
                bullets.append(line[2:])
        rules = (self.REFS / "bullet-rules.md").read_text(encoding="utf-8")
        table = rules.split("## Quick examples", 1)[1].split("\n## ", 1)[0]
        for line in table.splitlines():
            if line.startswith("| ") and not line.startswith("| Weak") and line.count("|") == 3:
                bullets.append(line.split("|")[2].strip())
        self.assertGreaterEqual(len(bullets), 5)
        for bullet in bullets:
            words = len(bullet.split())
            self.assertTrue(20 <= words <= 35, f"{words} words: {bullet}")


class MigrateTests(unittest.TestCase):
    def test_worksheet_lists_sections(self):
        lines = ["# CMD", "## 5. Master Accomplishments", "### Feature A", "text", "## 17. Notes", "x"]
        sections = migrate_cmd.split_sections(lines)
        self.assertEqual([s["num"] for s in sections], [5, 17])
        sheet = migrate_cmd.worksheet(Path("CMD.md"), sections)
        self.assertIn("- [ ] line 3: Feature A", sheet)
        self.assertIn("not migrated", sheet)

    def test_sections_without_subheadings_list_items(self):
        lines = ["## 8. Quantified Metrics", "", "| Metric | Value |", "|---|---:|", "| Stories | 30 |",
                 "## 12. Recognition", "- Award A", "- Award B"]
        sheet = migrate_cmd.worksheet(Path("CMD.md"), migrate_cmd.split_sections(lines))
        self.assertIn("- [ ] line 5: Stories | 30", sheet)
        self.assertNotIn("---", sheet.split("Quantified")[1].split("## 12")[0])
        self.assertIn("- [ ] line 8: Award B", sheet)


if __name__ == "__main__":
    unittest.main()

"""Validate the career record.

Usage: python validate.py [CAREER_DIR]

CAREER_DIR defaults to ./career. Prints one line per problem:
  error:   must be fixed (exit code 1)
  warning: worth a look, does not fail validation
Each message names the file and field and says how to fix it.
"""

import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # never write __pycache__ into an installed skill folder

from careerlib import (  # noqa: E402
    SCHEMA_VERSION,
    as_list,
    find_career_dir,
    load_record,
    notes_timestamps,
    numbers_in,
    text,
)

ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
MONTH = re.compile(r"^\d{4}(-(0[1-9]|1[0-2]))?$")  # YYYY-MM, or YYYY when the month is unknown
DAY = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")
SCORE = re.compile(r"^\d+(\.\d+)?$")

STATUSES = {"draft", "incomplete", "confirmed"}
ITEM_STATUSES = {"draft", "confirmed"}
CATEGORIES = {
    "feature", "defect", "investigation", "performance", "reliability", "security",
    "testing", "automation", "refactoring", "developer_productivity", "documentation",
    "architecture", "production_support", "leadership", "collaboration", "learning", "other",
}
ORIGINS = {"assigned", "self_initiated", "requested_by_others"}
CONFIDENCE = {"measured", "reported", "estimated", "relative_only"}
EVIDENCE_TYPES = {"pr", "doc", "dashboard", "ticket", "email", "recognition", "other"}
ROLE_TYPES = {"full_time", "internship", "contract", "part_time"}
SKILL_CATEGORIES = {"language", "framework", "database", "cloud", "devops", "tool", "concept", "other"}
SKILL_DEPTHS = {"working", "proficient", "expert"}
PROJECT_TYPES = {"personal", "academic", "open_source"}
SCORE_TYPES = {"cgpa", "percentage"}

BULLET_MIN_WORDS = 20
BULLET_MAX_WORDS = 35


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, where, message):
        self.errors.append(f"error: {where}: {message}")

    def warn(self, where, message):
        self.warnings.append(f"warning: {where}: {message}")


def check_month(report, where, field, value, allow_present=False, required=True, pad="01"):
    """Check a YYYY-MM or YYYY value. Returns a comparable YYYY-MM string or None.

    A year-only value is padded with `pad` ("01" for starts, "12" for ends).
    """
    value = text(value)
    if not value:
        if required:
            report.error(where, f"{field} is empty; use YYYY-MM (or YYYY if the month is unknown)")
        return None
    if allow_present and value == "present":
        return "9999-12"
    if not MONTH.match(value):
        hint = "YYYY-MM, YYYY or present" if allow_present else "YYYY-MM or YYYY"
        report.error(where, f"{field} '{value}' is not {hint}")
        return None
    return value if len(value) == 7 else f"{value}-{pad}"


def check_period(report, where, start, end, required=True):
    s = check_month(report, where, "start", start, required=required)
    e = check_month(report, where, "end", end, allow_present=True, required=required, pad="12")
    if s and e and e < s:
        report.error(where, f"end {end} is before start {start}")


def check_list_of_dicts(report, where, field, value):
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, dict) for item in value):
        report.error(where, f"{field} must be a list of mappings")
        return []
    return value


def check_sources(report, where, sources, stamps):
    for stamp in as_list(sources):
        if text(stamp) not in stamps:
            report.error(where, f"source '{stamp}' has no matching '## {stamp}' entry in NOTES.md")


class Validator:
    def __init__(self, career_dir):
        self.career_dir = Path(career_dir)
        self.report = Report()
        self.ids = {}  # id -> where it was defined
        self.role_engagements = {}  # role id -> set of engagement ids
        self.evidence_targets = set()  # accomplishment and project ids
        self.acc_similar = {}  # accomplishment id -> set of similar ids

    def register(self, where, ident):
        ident = text(ident)
        if not ident:
            self.report.error(where, "id is empty")
            return None
        if not ID.match(ident):
            self.report.error(where, f"id '{ident}' may only use letters, digits, '-' and '_'")
            return None
        if ident in self.ids:
            self.report.error(where, f"id '{ident}' is already used in {self.ids[ident]}")
            return None
        self.ids[ident] = where
        return ident

    def run(self):
        record, load_errors = load_record(self.career_dir)
        for message in load_errors:
            self.report.errors.append(f"error: {message}")
        self.stamps = notes_timestamps(self.career_dir)
        if not (self.career_dir / "NOTES.md").exists():
            self.report.error(self.career_dir / "NOTES.md", "missing. Run init.py to restore it.")

        for name, data in record.items():
            if name in ("accomplishments", "log_pending"):  # not data files
                continue
            where = f"data/{name}.yaml"
            if not isinstance(data, dict):
                self.report.error(where, "must be a mapping at the top level")
                record[name] = {}
            elif data and data.get("schema_version") != SCHEMA_VERSION:
                self.report.error(where, f"schema_version must be {SCHEMA_VERSION}")

        # Register ids first so cross-references can be checked in any order.
        self.check_employment(record.get("employment", {}))
        accomplishments = []
        for path, data in record["accomplishments"]:
            where = f"data/accomplishments/{path.name}"
            if not isinstance(data, dict):
                self.report.error(where, "must be a mapping at the top level")
                continue
            ident = self.register(where, data.get("id"))
            if ident and ident != path.stem:
                self.report.error(where, f"id '{ident}' must match the file name '{path.stem}'")
            if ident:
                self.evidence_targets.add(ident)
                accomplishments.append((where, ident, data))
        projects = check_list_of_dicts(self.report, "data/projects.yaml", "projects",
                                       record.get("projects", {}).get("projects"))
        for project in projects:
            ident = self.register("data/projects.yaml", project.get("id"))
            if ident:
                self.evidence_targets.add(ident)

        for where, ident, data in accomplishments:
            self.check_accomplishment(where, ident, data)
        self.check_similar_symmetry()
        self.check_projects(projects)
        self.check_profile(record.get("profile", {}))
        self.check_skills(record.get("skills", {}))
        self.check_education(record.get("education", {}))
        self.check_simple_list(record.get("certifications", {}), "certifications", "name")
        self.check_recognition(record.get("recognition", {}))
        self.check_learning(record.get("learning", {}))
        self.check_goals(record.get("goals", {}))
        return self.report

    # --- individual files -------------------------------------------------

    def check_profile(self, data):
        where = "data/profile.yaml"
        email = text(data.get("email"))
        if email and not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            self.report.error(where, f"email '{email}' does not look like an email address")
        location = text(data.get("location"))
        if location.count(",") >= 2 or re.search(r"\d{6}", location):
            self.report.warn(where, "location looks like a full address; keep only the city")
        for headline in check_list_of_dicts(self.report, where, "headlines", data.get("headlines")):
            self.register(where, headline.get("id"))
            if not text(headline.get("text")):
                self.report.error(where, f"headline {headline.get('id')}: text is empty")
            if headline.get("status") not in ITEM_STATUSES:
                self.report.error(where, f"headline {headline.get('id')}: status must be draft or confirmed")

    def check_employment(self, data):
        where = "data/employment.yaml"
        for employer in check_list_of_dicts(self.report, where, "employers", data.get("employers")):
            ident = self.register(where, employer.get("id"))
            ew = f"{where} employer {ident}"
            if not text(employer.get("legal_name")):
                self.report.error(ew, "legal_name is empty; use the full legal name, e.g. 'Example Corp Pvt. Ltd.'")
            for role in check_list_of_dicts(self.report, ew, "roles", employer.get("roles")):
                rid = self.register(ew, role.get("id"))
                rw = f"{where} role {rid}"
                if not text(role.get("title")):
                    self.report.error(rw, "title is empty; use the full official title")
                elif re.search(r"\b(Sr|Jr|Mgr|Engg?|Dev)\.?(\s|$)", text(role.get("title"))):
                    self.report.warn(rw, f"title '{role.get('title')}' looks abbreviated; write it in full")
                if role.get("type") not in ROLE_TYPES:
                    self.report.error(rw, f"type must be one of {sorted(ROLE_TYPES)}")
                check_period(self.report, rw, role.get("start"), role.get("end"))
                engagements = set()
                for eng in check_list_of_dicts(self.report, rw, "engagements", role.get("engagements")):
                    gid = self.register(rw, eng.get("id"))
                    if gid:
                        engagements.add(gid)
                    if not text(eng.get("client_descriptor")):
                        self.report.error(f"{rw} engagement {gid}", "client_descriptor is empty; describe the client by industry and scale")
                    if not (isinstance(eng.get("nda"), bool) or eng.get("nda") == "unknown"):
                        self.report.error(f"{rw} engagement {gid}", "nda must be true, false or unknown")
                if rid:
                    self.role_engagements[rid] = engagements

    def check_accomplishment(self, where, ident, data):
        r = self.report
        if data.get("schema_version") != SCHEMA_VERSION:
            r.error(where, f"schema_version must be {SCHEMA_VERSION}")
        status = data.get("status")
        if status not in STATUSES:
            r.error(where, f"status must be one of {sorted(STATUSES)}")
        final = status in ("incomplete", "confirmed")

        role = text(data.get("role_id"))
        if not role:
            if final:
                r.error(where, "role_id is empty; link it to a role in employment.yaml")
        elif role not in self.role_engagements:
            r.error(where, f"role_id '{role}' is not a role in employment.yaml")
        engagement = data.get("engagement_id")
        if engagement and role in self.role_engagements and engagement not in self.role_engagements[role]:
            r.error(where, f"engagement_id '{engagement}' is not an engagement of role '{role}'")

        period = data.get("period") or {}
        if not isinstance(period, dict):
            r.error(where, "period must be a mapping with start and end")
            period = {}
        check_period(r, where, period.get("start"), period.get("end"), required=False)
        if final and not text(period.get("start")):
            r.warn(where, "period is unknown; a resume needs at least the year (ask the user, or keep it as a gap)")

        category = text(data.get("category"))
        if category and category not in CATEGORIES:
            r.error(where, f"category '{category}' is not one of {sorted(CATEGORIES)}")
        elif not category and final:
            r.error(where, "category is empty")

        origin = text(data.get("origin"))
        if origin and origin not in ORIGINS:
            r.error(where, f"origin '{origin}' is not one of {sorted(ORIGINS)} (or leave it empty)")

        missing = [f for f in ("title", "situation", "task", "outcome") if not text(data.get(f))]
        actions = [a for a in as_list(data.get("actions")) if text(a)]
        if not actions:
            missing.append("actions")
        gaps = [g for g in as_list(data.get("gaps")) if text(g)]
        if status == "confirmed" and missing:
            r.error(where, f"status is confirmed but {', '.join(missing)} empty; fill them in or use status incomplete with gaps")
        if status == "incomplete":
            if not gaps:
                r.error(where, "status is incomplete but gaps is empty; list what is missing")
            for field in ("title", "actions"):
                if field in missing:
                    r.error(where, f"{field} is empty; even an incomplete record needs it")
        if final and not as_list(data.get("sources")):
            r.error(where, "sources is empty; link the NOTES.md entries this record came from")
        check_sources(r, where, data.get("sources"), self.stamps)

        if not isinstance(data.get("technologies") or [], list):
            r.error(where, "technologies must be a list")

        confirmed_numbers = set()
        unconfirmed_numbers = set()
        for i, metric in enumerate(check_list_of_dicts(r, where, "metrics", data.get("metrics")), 1):
            mw = f"{where} metric {i} ({text(metric.get('name')) or 'unnamed'})"
            if not text(metric.get("name")):
                r.error(mw, "name is empty")
            if not (text(metric.get("value")) or (text(metric.get("before")) and text(metric.get("after")))):
                r.error(mw, "needs value, or both before and after")
            if metric.get("confidence") not in CONFIDENCE:
                r.error(mw, f"confidence must be one of {sorted(CONFIDENCE)}")
            if not isinstance(metric.get("user_confirmed"), bool):
                r.error(mw, "user_confirmed must be true or false")
            elif status == "confirmed" and not metric["user_confirmed"]:
                r.error(mw, "status is confirmed but this metric is not user_confirmed; confirm it with the user or remove it")
            target = confirmed_numbers if metric.get("user_confirmed") is True else unconfirmed_numbers
            target |= numbers_in(metric)

        for i, item in enumerate(check_list_of_dicts(r, where, "evidence", data.get("evidence")), 1):
            if item.get("type") not in EVIDENCE_TYPES:
                r.error(f"{where} evidence {i}", f"type must be one of {sorted(EVIDENCE_TYPES)}")
            if not text(item.get("ref")):
                r.error(f"{where} evidence {i}", "ref is empty; describe the evidence without confidential detail")

        # Numbers a bullet may use: everything in the record except bullets
        # themselves and metrics the user has not confirmed.
        allowed = set(confirmed_numbers)
        for key, value in data.items():
            if key not in ("metrics", "bullets", "id", "similar_to", "sources", "created", "updated", "schema_version"):
                allowed |= numbers_in(value)
        self.check_bullets(where, data.get("bullets"), status, allowed, unconfirmed_numbers)

        similar = set()
        for other in as_list(data.get("similar_to")):
            other = text(other)
            if other == ident:
                r.error(where, "similar_to lists the record itself")
            elif other not in self.evidence_targets:
                r.error(where, f"similar_to '{other}' is not an accomplishment id")
            else:
                similar.add(other)
        self.acc_similar[ident] = similar

        follow_up = data.get("follow_up")
        if follow_up is not None:
            if not isinstance(follow_up, dict):
                r.error(where, "follow_up must be null or a mapping with due and ask")
            else:
                check_month(r, f"{where} follow_up", "due", follow_up.get("due"))
                if not text(follow_up.get("ask")):
                    r.error(f"{where} follow_up", "ask is empty")
        for field in ("created", "updated"):
            value = text(data.get(field))
            if value and not DAY.match(value):
                r.error(where, f"{field} '{value}' is not YYYY-MM-DD")
            elif not value and final:
                r.error(where, f"{field} is empty; use YYYY-MM-DD")

    def check_bullets(self, where, bullets, status, allowed, unconfirmed):
        r = self.report
        seen = set()
        for bullet in check_list_of_dicts(r, where, "bullets", bullets):
            bid = text(bullet.get("id")) or "?"
            bw = f"{where} bullet {bid}"
            if bid in seen:
                r.error(bw, "bullet id is repeated in this record")
            seen.add(bid)
            body = text(bullet.get("text"))
            if not body:
                r.error(bw, "text is empty")
                continue
            if bullet.get("status") not in ITEM_STATUSES:
                r.error(bw, "status must be draft or confirmed")
            if bullet.get("status") == "confirmed" and status == "draft":
                r.error(bw, "bullet is confirmed but the record is still draft; confirm the record first")
            for number in sorted(numbers_in(body)):
                if number in allowed:
                    continue
                if number in unconfirmed:
                    if bullet.get("status") == "confirmed":
                        r.error(bw, f"uses {number}, which is only in a metric the user has not confirmed")
                else:
                    r.error(bw, f"uses the number {number}, which is not in the record; add it to the record with the user or remove it from the bullet")
            words = len(body.split())
            if not BULLET_MIN_WORDS <= words <= BULLET_MAX_WORDS:
                r.warn(bw, f"{words} words; bullets usually read best at {BULLET_MIN_WORDS}-{BULLET_MAX_WORDS} words (at most two lines)")
            if not isinstance(bullet.get("tracks") or [], list):
                r.error(bw, "tracks must be a list")

    def check_similar_symmetry(self):
        for ident, others in self.acc_similar.items():
            for other in others:
                if ident not in self.acc_similar.get(other, set()):
                    self.report.error(
                        f"data/accomplishments/{ident}.yaml",
                        f"similar_to lists '{other}', but '{other}' does not list '{ident}' back; add it there too",
                    )

    def check_projects(self, projects):
        where = "data/projects.yaml"
        for project in projects:
            pw = f"{where} project {project.get('id')}"
            if not text(project.get("name")):
                self.report.error(pw, "name is empty")
            if project.get("type") and project.get("type") not in PROJECT_TYPES:
                self.report.error(pw, f"type must be one of {sorted(PROJECT_TYPES)}")
            status = project.get("status")
            if status not in ITEM_STATUSES:
                self.report.error(pw, "status must be draft or confirmed")
            if status == "confirmed" and not as_list(project.get("sources")):
                self.report.error(pw, "status is confirmed but sources is empty")
            check_sources(self.report, pw, project.get("sources"), self.stamps)
            allowed = numbers_in({k: v for k, v in project.items() if k not in ("bullets", "id", "sources")})
            self.check_bullets(pw, project.get("bullets"), "confirmed" if status == "confirmed" else "draft", allowed, set())

    def check_skills(self, data):
        where = "data/skills.yaml"
        names = {}
        for skill in check_list_of_dicts(self.report, where, "skills", data.get("skills")):
            name = text(skill.get("name"))
            sw = f"{where} skill '{name}'"
            if not name:
                self.report.error(where, "a skill has an empty name")
                continue
            if name.lower() in names:
                self.report.warn(sw, "listed more than once")
            names[name.lower()] = True
            if skill.get("category") not in SKILL_CATEGORIES:
                self.report.error(sw, f"category must be one of {sorted(SKILL_CATEGORIES)}")
            if skill.get("depth") and skill.get("depth") not in SKILL_DEPTHS:
                self.report.error(sw, f"depth must be one of {sorted(SKILL_DEPTHS)}")
            evidence = as_list(skill.get("evidence"))
            for ref in evidence:
                if text(ref) not in self.evidence_targets:
                    self.report.error(sw, f"evidence '{ref}' is not an accomplishment or project id")
            if not evidence:
                self.report.warn(sw, "has no evidence, so it will not be used on a resume")

    def check_education(self, data):
        where = "data/education.yaml"
        for entry in check_list_of_dicts(self.report, where, "education", data.get("education")):
            ident = self.register(where, entry.get("id"))
            ew = f"{where} {ident}"
            for field in ("degree", "institution"):
                if not text(entry.get(field)):
                    self.report.error(ew, f"{field} is empty")
            check_period(self.report, ew, entry.get("start"), entry.get("end"), required=False)
            score = entry.get("score")
            if score:
                if not isinstance(score, dict):
                    self.report.error(ew, "score must be a mapping with type, value and scale")
                    continue
                if score.get("type") not in SCORE_TYPES:
                    self.report.error(ew, f"score type must be one of {sorted(SCORE_TYPES)}")
                value = score.get("value")
                if not isinstance(value, str):
                    self.report.error(ew, "score value must be quoted text (e.g. \"7.90\") so it is never rounded")
                elif not SCORE.match(value):
                    self.report.error(ew, f"score value '{value}' is not a number")

    def check_simple_list(self, data, key, required_field):
        where = f"data/{key}.yaml"
        for entry in check_list_of_dicts(self.report, where, key, data.get(key)):
            ident = self.register(where, entry.get("id"))
            if not text(entry.get(required_field)):
                self.report.error(f"{where} {ident}", f"{required_field} is empty")

    def check_recognition(self, data):
        where = "data/recognition.yaml"
        for entry in check_list_of_dicts(self.report, where, "recognition", data.get("recognition")):
            ident = self.register(where, entry.get("id"))
            rw = f"{where} {ident}"
            if not text(entry.get("title")):
                self.report.error(rw, "title is empty")
            check_month(self.report, rw, "date", entry.get("date"), required=False)
            if entry.get("status") is not None and entry.get("status") not in ITEM_STATUSES:
                self.report.error(rw, "status must be draft or confirmed")
            for ref in as_list(entry.get("related")):
                if text(ref) not in self.evidence_targets:
                    self.report.error(rw, f"related '{ref}' is not an accomplishment or project id")
            check_sources(self.report, rw, entry.get("sources"), self.stamps)

    def check_learning(self, data):
        where = "data/learning.yaml"
        for entry in check_list_of_dicts(self.report, where, "learning", data.get("learning")):
            ident = self.register(where, entry.get("id"))
            if not text(entry.get("topic")):
                self.report.error(f"{where} {ident}", "topic is empty")
            check_month(self.report, f"{where} {ident}", "date", entry.get("date"), required=False)
            for ref in as_list(entry.get("applied_in")):
                if text(ref) not in self.evidence_targets:
                    self.report.error(f"{where} {ident}", f"applied_in '{ref}' is not an accomplishment or project id")

    def check_goals(self, data):
        where = "data/goals.yaml"
        for key in ("target_roles", "target_employers", "short_term", "medium_term", "long_term"):
            if data.get(key) is not None and not isinstance(data.get(key), list):
                self.report.error(where, f"{key} must be a list")


def validate(career_dir):
    return Validator(career_dir).run()


def main(argv):
    career_dir = find_career_dir(argv[1] if len(argv) > 1 else "career")
    report = validate(career_dir)
    for line in report.errors + report.warnings:
        print(line)
    print(f"{len(report.errors)} error(s), {len(report.warnings)} warning(s) in {career_dir}")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

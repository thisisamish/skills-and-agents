"""Shared helpers for the career record scripts.

Imported by the other scripts in this folder. Requires PyYAML.
"""

import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only without PyYAML
    sys.stderr.write(
        "PyYAML is not installed for this Python.\n"
        "Run the setup-career-skills skill, or create the record's virtual environment:\n"
        "  uv venv career/.venv && uv pip install --python career/.venv pyyaml\n"
    )
    sys.exit(2)

SCHEMA_VERSION = 1

# Data files that hold a single YAML document each, relative to career/data/.
DATA_FILES = [
    "profile.yaml",
    "employment.yaml",
    "skills.yaml",
    "education.yaml",
    "projects.yaml",
    "certifications.yaml",
    "recognition.yaml",
    "learning.yaml",
    "goals.yaml",
]

ACCOMPLISHMENT_DIR = "accomplishments"

NOTES_HEADING = re.compile(r"^## (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:\d{2}))\s*$")


class _StringDateLoader(yaml.SafeLoader):
    """SafeLoader that keeps dates and timestamps as plain strings.

    Without this, PyYAML turns 2025-03-14 into a date object and
    2025-03-14T10:00:00+05:30 into a datetime, which breaks comparisons
    with NOTES.md headings.
    """


_StringDateLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def load_yaml(path):
    """Load one YAML file. Returns (data, error_message)."""
    try:
        with open(path, encoding="utf-8") as handle:
            return yaml.load(handle, Loader=_StringDateLoader), None
    except yaml.YAMLError as exc:
        return None, f"{path}: invalid YAML: {exc}"
    except OSError as exc:
        return None, f"{path}: cannot read: {exc}"


def dump_yaml(data):
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)


def find_career_dir(arg):
    """Resolve the career/ directory from a command-line argument."""
    path = Path(arg).resolve()
    if path.name != "career" and (path / "career").is_dir():
        path = path / "career"
    return path


def load_record(career_dir):
    """Load every data file and accomplishment.

    Returns (record, errors) where record is a dict with one key per data
    file stem plus "accomplishments" (a list of (path, data) pairs).
    """
    career_dir = Path(career_dir)
    data_dir = career_dir / "data"
    record = {"accomplishments": []}
    errors = []
    if not data_dir.is_dir():
        errors.append(f"{data_dir}: not found. Run init.py to create the career record.")
        return record, errors
    for name in DATA_FILES:
        path = data_dir / name
        stem = name[: -len(".yaml")]
        if not path.exists():
            errors.append(f"{path}: missing. Run init.py to restore blank files.")
            record[stem] = {}
            continue
        data, err = load_yaml(path)
        if err:
            errors.append(err)
            data = {}
        record[stem] = data or {}
    acc_dir = data_dir / ACCOMPLISHMENT_DIR
    if acc_dir.is_dir():
        for path in sorted(acc_dir.glob("*.yaml")):
            data, err = load_yaml(path)
            if err:
                errors.append(err)
                continue
            record["accomplishments"].append((path, data or {}))
    return record, errors


def notes_timestamps(career_dir):
    """Return the set of entry timestamps (## headings) in NOTES.md."""
    path = Path(career_dir) / "NOTES.md"
    stamps = set()
    if not path.exists():
        return stamps
    for line in path.read_text(encoding="utf-8").splitlines():
        # Only real headings at column 0 count, not indented examples.
        match = NOTES_HEADING.match(line.rstrip())
        if match:
            stamps.add(match.group(1))
    return stamps


def as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def text(value):
    """Normalise an optional scalar to a stripped string."""
    if value is None:
        return ""
    return str(value).strip()


NUMBER = re.compile(r"\d+(?:[.,]\d+)*")


def numbers_in(value):
    """Return the set of normalised numbers that appear in a string or nested data.

    "12,000" -> "12000", "2.1M" -> "2.1", "99.95%" -> "99.95".
    """
    found = set()

    def walk(item):
        if item is None:
            return
        if isinstance(item, dict):
            for sub in item.values():
                walk(sub)
        elif isinstance(item, list):
            for sub in item:
                walk(sub)
        elif isinstance(item, bool):
            return
        else:
            for match in NUMBER.findall(str(item)):
                found.add(_normalise_number(match))

    walk(value)
    return found


def _normalise_number(token):
    # Treat commas as thousands separators ("12,000") unless the token looks
    # like a decimal written with a comma ("2,5").
    if "," in token and re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", token):
        token = token.replace(",", "")
    token = token.replace(",", ".")
    try:
        return format(Decimal(token).normalize(), "f")
    except InvalidOperation:
        return token

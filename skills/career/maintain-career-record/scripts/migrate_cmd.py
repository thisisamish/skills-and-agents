"""Write a migration worksheet for a legacy Career Master Document (CMD.md).

Usage: python migrate_cmd.py LEGACY_CMD_MD [OUTPUT_MD]

Splits the legacy file at its numbered "## N." sections and writes a
checklist that maps every section and sub-heading to its new home in
career/data/. The agent then fills in the YAML by hand, ticking items off.
OUTPUT_MD defaults to migration-worksheet.md next to the legacy file.
Uses only the standard library.
"""

import re
import sys
from pathlib import Path

SECTION = re.compile(r"^##\s+(\d+)\.\s+(.*)$")
SUBSECTION = re.compile(r"^###\s+(.*)$")
ITEM = re.compile(r"^(?:[-*]\s+|\|\s*(?!-))(.+)$")  # list items and table rows (not separators)

TARGETS = {
    1: "profile.yaml (contact) and goals.yaml (objectives); metadata itself is not migrated",
    2: "profile.yaml headlines (status draft), keeping the user's wording",
    3: "employment.yaml (employers, roles, engagements); education entries go to education.yaml",
    4: "employment.yaml role summary and engagements (client descriptors, nda flag)",
    5: "accomplishments/<id>.yaml — one file per accomplishment",
    6: "bullets on the matching accomplishment; list unmatched bullets for the user",
    7: "merge into the matching accomplishment's situation/task/actions/outcome and interview fields",
    8: "metrics on the matching accomplishment (confidence and user_confirmed from NOTES.md); unmatched metrics go to the role's notes",
    9: "skills.yaml, each skill linked to evidence ids",
    10: "skills.yaml (category: concept) with evidence ids",
    11: "documentation accomplishments (category: documentation) or recognition.yaml",
    12: "recognition.yaml",
    13: "projects.yaml (professional projects become accomplishments or role summaries)",
    14: "learning.yaml",
    15: "goals.yaml",
    16: "gaps on the matching records",
    17: "not migrated (regenerable); keep in legacy/ for reference",
    18: "not migrated (regenerable); keep in legacy/ for reference",
}


def split_sections(lines):
    sections = []
    current = None
    for number, line in enumerate(lines, 1):
        match = SECTION.match(line)
        if match:
            current = {"num": int(match.group(1)), "title": match.group(2).strip(),
                       "start": number, "subs": [], "items": []}
            sections.append(current)
        elif current is not None:
            sub = SUBSECTION.match(line)
            if sub:
                current["subs"].append((number, sub.group(1).strip()))
            else:
                item = ITEM.match(line.strip())
                if item and line.strip():
                    current["items"].append((number, item.group(1).strip().rstrip("|").strip()))
        if current is not None:
            current["end"] = number
    return sections


def worksheet(legacy_path, sections):
    out = [
        "# Migration worksheet",
        "",
        f"Source: `{legacy_path.name}`. Follow references/migration.md in maintain-career-record.",
        "Tick each item once its content is in career/data/ (or deliberately not migrated).",
        "",
    ]
    for section in sections:
        target = TARGETS.get(section["num"], "no default mapping — decide with the user")
        out.append(f"## {section['num']}. {section['title']} (lines {section['start']}–{section['end']})")
        out.append("")
        out.append(f"Goes to: {target}")
        out.append("")
        if section["subs"]:
            for line_no, title in section["subs"]:
                out.append(f"- [ ] line {line_no}: {title}")
        elif section["items"]:
            # No sub-headings: track each list item or table row (the first row may be a header).
            for line_no, title in section["items"]:
                short = title if len(title) <= 90 else title[:87] + "..."
                out.append(f"- [ ] line {line_no}: {short}")
        else:
            out.append("- [ ] whole section")
        out.append("")
    if not sections:
        out.append("No numbered '## N.' sections found. Map the document by hand with the user.")
    return "\n".join(out) + "\n"


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    legacy = Path(argv[1])
    if not legacy.is_file():
        print(f"error: {legacy} not found")
        return 1
    output = Path(argv[2]) if len(argv) > 2 else legacy.with_name("migration-worksheet.md")
    if output.exists():
        print(f"error: {output} already exists; delete it or pass another output path")
        return 1
    sections = split_sections(legacy.read_text(encoding="utf-8").splitlines())
    output.write_text(worksheet(legacy, sections), encoding="utf-8")
    print(f"wrote {output} ({len(sections)} sections)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

"""Create the career record in a user's repo from the blank templates.

Usage: python init.py [REPO_ROOT]

Creates REPO_ROOT/career/ (default: the current directory). Never
overwrites an existing file; prints what it created and what it kept.
Uses only the standard library so it can run before PyYAML is installed.
"""

import shutil
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"

GITIGNORE = ".venv/\n__pycache__/\n"


def init(repo_root):
    career = Path(repo_root).resolve() / "career"
    created, kept = [], []

    def place(target, write):
        if target.exists():
            kept.append(target)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            write(target)
            created.append(target)

    for source in sorted((TEMPLATES / "data").rglob("*")):
        if source.is_file():
            target = career / "data" / source.relative_to(TEMPLATES / "data")
            place(target, lambda t, s=source: shutil.copyfile(s, t))
    place(career / "NOTES.md", lambda t: shutil.copyfile(TEMPLATES / "NOTES.md", t))
    place(career / "log.md", lambda t: shutil.copyfile(TEMPLATES / "log.md", t))
    place(career / ".gitignore", lambda t: t.write_text(GITIGNORE, encoding="utf-8"))
    return career, created, kept


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    career, created, kept = init(root)
    print(f"Career record: {career}")
    for path in created:
        print(f"  created {path.relative_to(career)}")
    for path in kept:
        print(f"  kept    {path.relative_to(career)} (already exists)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

---
name: setup-career-skills
description: Sets up the career skills suite in the user's repository. Checks that every career skill is installed, creates a Python virtual environment for the record with uv (PyYAML only, never a global install), creates the career/ record from blank templates, and detects an old CMD.md, whose migration it hands to maintain-career-record. Use when the user asks to set up, install or initialise career tracking, runs setup-career-skills, or when another career skill reports that career/ or its Python environment is missing.
compatibility: Part of the career skills suite (setup-career-skills, maintain-career-record, capture-work-experience); install all of them together. Uses uv (preferred) or Python 3.9+.
metadata:
  version: 1.0.0
  suite: career
---

# Set up career skills

Prepare the user's repository so the other career skills can run. Run every command from the root of the user's repository, never from the skills' own folder.

Copy this checklist into your reply and tick it off:

```
- [ ] 1. Confirm where the record should live
- [ ] 2. Check the whole suite is installed
- [ ] 3. Create the Python environment
- [ ] 4. Create the record
- [ ] 5. Verify
- [ ] 6. Check for legacy data and report next steps
```

## 1. Confirm where the record should live

The record goes in `career/` at the root of the user's current repository; it holds personal data, so it belongs in a private repository. If the current folder is the repository that contains these skills, or isn't a repository the user owns, stop and ask where their career data should live. If the repository has a remote, remind the user to keep it private.

- If `career/data/` already exists, setup has run before: skip to step 3 and repair only what is missing.
- If `career/CMD.md` or `career/EXPERIENCE_DB.md` exists (legacy data), check that the repository has no uncommitted changes before creating anything. If it has, ask the user to commit first, so the migration can be reviewed and undone.

## 2. Check the whole suite is installed

The skills are siblings in one folder. From this skill's folder, check that these exist:

- `../maintain-career-record/SKILL.md` and `../maintain-career-record/scripts/init.py`
- `../capture-work-experience/SKILL.md`

If any is missing, stop. Tell the user the career skills must be installed together, as described in the README of the skills repository, and that setup can't continue until they are.

Below, `SCRIPTS` means the full path of `../maintain-career-record/scripts/`.

## 3. Create the Python environment

The record's environment is `career/.venv`. Its Python, written `PY` below, is `career/.venv/Scripts/python.exe` on Windows and `career/.venv/bin/python` elsewhere. Always call it by this path, which also sidesteps any other virtual environment that happens to be active. Never install packages globally.

1. Run `uv --version`. If it isn't found, look for an installed uv that isn't on PATH yet: `~/.local/bin/uv`, `%LOCALAPPDATA%/Microsoft/WinGet/Links/uv.exe`, or a `uv.exe` under `%LOCALAPPDATA%/Microsoft/WinGet/Packages/astral-sh.uv*`. If you find one, use its full path, and tell the user that restarting their terminal will put it on PATH.
2. **If uv is available:**
   ```
   uv venv career/.venv --python ">=3.9"
   uv pip install --python career/.venv -r SCRIPTS/requirements.txt
   ```
   uv downloads a suitable Python if none is installed.
3. **If uv is missing:** ask the user whether to install it. The official options are `winget install --id astral-sh.uv` (Windows), `brew install uv` (macOS), or the installer at https://docs.astral.sh/uv/getting-started/installation/. Install only with their agreement, then go back to step 3.2. If they decline, use an existing Python 3.9+ instead. Check with `python3 --version`, `python --version` or `py -3 --version`, whichever reports a version first, and call it `BASE` here. Then run:
   ```
   BASE -m venv career/.venv
   PY -m pip install -r SCRIPTS/requirements.txt
   ```
   This pip runs inside the virtual environment, not globally.
4. If `career/.venv` already exists but `PY -c "import yaml"` fails, run only the install command for whichever path you used.

## 4. Create the record

**If legacy data exists** (step 1), don't run `init.py` here. If the user has already asked for the migration, go straight to maintain-career-record's migration guide (`../maintain-career-record/references/migration.md`): it moves the old file aside, runs `init.py`, migrates and validates. If they haven't asked, offer the migration and wait for their answer. Run `init.py` and continue with step 5 only if they decline.

Otherwise:

```
PY SCRIPTS/init.py .
```

`init.py` creates `career/data/`, `career/NOTES.md` and `career/.gitignore`, which ignores `.venv/`. It never overwrites existing files, so it's safe to re-run.

## 5. Verify

```
PY -c "import yaml; print(yaml.__version__)"
PY SCRIPTS/validate.py career
PY SCRIPTS/render.py career
```

Validation must report 0 errors. A blank record validates cleanly. If it doesn't, read the messages: a file that existed before setup may need migrating (step 6).

## 6. Check for legacy data and report next steps

- If legacy data was found and not migrated, remind the user that maintain-career-record can migrate it whenever they want.
- Otherwise, suggest starting with maintain-career-record for profile, employers and roles, then capture-work-experience for individual pieces of work.
- Remind the user to commit `career/`. `.venv/` stays out of git.

Report what was created, which Python and PyYAML versions are in use, and the validation result.

## Troubleshooting

- **"No Python at …" or a similar error from `python`:** a stale virtual environment is active (the `VIRTUAL_ENV` variable is set). Use uv, or run `PY` by its full path. Suggest the user deactivate the old environment.
- **uv can't download Python (offline or blocked):** use the fallback path in step 3.3 with an installed Python.
- **pip says the environment is externally managed:** you're not using the virtual environment's Python. Use `PY -m pip`, never the system pip.
- **Permission denied writing `career/`:** ask the user to fix permissions or choose another repository. Don't write anywhere else.

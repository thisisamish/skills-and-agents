"""Print the current local time as an ISO 8601 timestamp for a NOTES.md heading.

Usage: python timestamp.py
Example output: 2025-03-14T10:02:00+05:30
"""

import datetime

if __name__ == "__main__":
    print(datetime.datetime.now().astimezone().isoformat(timespec="seconds"))

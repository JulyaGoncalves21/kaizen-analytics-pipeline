from __future__ import annotations

import csv
from pathlib import Path

REQUIRED_FIELDS = {"kaizen_id", "category", "completion_date"}


def read_public_record(path: Path) -> dict[str, str]:
    """Read the deliberately simple key/value CSV used by the public demo."""
    with path.open(encoding="utf-8-sig", newline="") as stream:
        values = {row["field"].strip(): row["value"].strip() for row in csv.DictReader(stream)}
    missing = REQUIRED_FIELDS - values.keys()
    if missing:
        raise ValueError(f"missing required fields: {', '.join(sorted(missing))}")
    return values

from __future__ import annotations

import csv
from pathlib import Path

from .models import RegistryRecord


def read_registry(path: Path) -> list[RegistryRecord]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return [RegistryRecord(**row) for row in csv.DictReader(stream)]


def read_validations(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return {
            row["kaizen_id"].strip()
            for row in csv.DictReader(stream)
            if row.get("validated", "").strip().lower() in {"true", "1", "yes"}
        }

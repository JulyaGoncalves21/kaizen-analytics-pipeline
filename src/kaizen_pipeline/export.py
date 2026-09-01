from __future__ import annotations

import csv
import json
from pathlib import Path

from .models import ProcessedRecord


def export_records(records: list[ProcessedRecord], output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = [record.to_dict() for record in records]
    csv_path = output_dir / "kaizens_public.csv"
    json_path = output_dir / "kaizens_public.json"
    with csv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]) if rows else [])
        if rows:
            writer.writeheader()
            writer.writerows(rows)
    json_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    return csv_path, json_path

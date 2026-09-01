from __future__ import annotations

import argparse
import logging

from .config import Settings
from .data_sources import read_registry, read_validations
from .export import export_records
from .file_discovery import locate
from .models import ProcessedRecord
from .transformation import build_record
from .validation import validate_record
from .workbook_reader import read_public_record

LOGGER = logging.getLogger(__name__)


def run(settings: Settings) -> list[ProcessedRecord]:
    validated = read_validations(settings.validations)
    results: list[ProcessedRecord] = []
    for registry in read_registry(settings.registry):
        located = locate(registry.expected_file, settings.inbox, settings.remote_fallback)
        if located.path is None:
            results.append(
                build_record(registry, {}, located.source, validated, ["source file not found"])
            )
            continue
        try:
            values = read_public_record(located.path)
            results.append(
                build_record(
                    registry,
                    values,
                    located.source,
                    validated,
                    validate_record(registry.kaizen_id, values),
                )
            )
        except (OSError, ValueError, KeyError) as exc:
            LOGGER.warning("Could not process %s: %s", registry.kaizen_id, exc)
            results.append(
                build_record(
                    registry, {}, located.source, validated, ["source file could not be processed"]
                )
            )
    export_records(results, settings.output)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the local synthetic Kaizen pipeline.")
    parser.add_argument("--show-summary", action="store_true")
    args = parser.parse_args()
    records = run(Settings.from_environment())
    if args.show_summary:
        publishable = sum(record.publishable for record in records)
        print(
            f"processed={len(records)} publishable={publishable} pending={len(records) - publishable}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

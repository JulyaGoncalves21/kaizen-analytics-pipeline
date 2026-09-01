from pathlib import Path

from kaizen_pipeline.file_discovery import locate
from kaizen_pipeline.validation import validate_record


def test_local_file_has_priority(tmp_path: Path) -> None:
    local = tmp_path / "local"
    fallback = tmp_path / "fallback"
    local.mkdir()
    fallback.mkdir()
    (local / "item.csv").write_text("local", encoding="utf-8")
    (fallback / "item.csv").write_text("fallback", encoding="utf-8")
    found = locate("item.csv", local, fallback)
    assert found.source == "local"
    assert found.path == local / "item.csv"


def test_fallback_is_used_when_local_is_missing(tmp_path: Path) -> None:
    local = tmp_path / "local"
    fallback = tmp_path / "fallback"
    local.mkdir()
    fallback.mkdir()
    (fallback / "item.csv").write_text("fallback", encoding="utf-8")
    assert locate("item.csv", local, fallback).source == "fallback"


def test_validation_reports_identifier_and_date() -> None:
    problems = validate_record(
        "KZ-001", {"kaizen_id": "KZ-999", "category": "Flow", "completion_date": "not-a-date"}
    )
    assert problems == ["identifier mismatch", "invalid completion date"]

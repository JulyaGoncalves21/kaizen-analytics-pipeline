from __future__ import annotations

from datetime import date


def validate_record(registry_id: str, values: dict[str, str]) -> list[str]:
    problems: list[str] = []
    if values.get("kaizen_id") != registry_id:
        problems.append("identifier mismatch")
    try:
        date.fromisoformat(values.get("completion_date", ""))
    except ValueError:
        problems.append("invalid completion date")
    if not values.get("category", "").strip():
        problems.append("category is empty")
    return problems

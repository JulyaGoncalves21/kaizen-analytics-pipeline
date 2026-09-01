from __future__ import annotations

from .models import ProcessedRecord, RegistryRecord


def build_record(
    registry: RegistryRecord,
    values: dict[str, str],
    source: str,
    validated_ids: set[str],
    problems: list[str],
) -> ProcessedRecord:
    validated = registry.kaizen_id in validated_ids
    return ProcessedRecord(
        kaizen_id=registry.kaizen_id,
        title=registry.title,
        owner=registry.owner,
        status=registry.status,
        source=source,
        category=values.get("category", ""),
        completion_date=values.get("completion_date", ""),
        business_validated=validated,
        publishable=validated and not problems,
        pending_reason="; ".join(problems)
        if problems
        else ("" if validated else "business validation required"),
    )

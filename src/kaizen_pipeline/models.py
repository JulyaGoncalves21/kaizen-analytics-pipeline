from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class RegistryRecord:
    kaizen_id: str
    title: str
    owner: str
    expected_file: str
    status: str


@dataclass(frozen=True)
class ProcessedRecord:
    kaizen_id: str
    title: str
    owner: str
    status: str
    source: str
    category: str
    completion_date: str
    business_validated: bool
    publishable: bool
    pending_reason: str = ""

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

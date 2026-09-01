from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    inbox: Path
    remote_fallback: Path
    registry: Path
    validations: Path
    output: Path

    @classmethod
    def from_environment(cls) -> Settings:
        return cls(
            inbox=Path(os.getenv("KAIZEN_INBOX", "sample-data/individual")),
            remote_fallback=Path(
                os.getenv("KAIZEN_REMOTE_FALLBACK", "sample-data/remote-fallback")
            ),
            registry=Path(os.getenv("KAIZEN_REGISTRY", "sample-data/improvement_registry.csv")),
            validations=Path(
                os.getenv("KAIZEN_VALIDATIONS", "sample-data/business_validations.csv")
            ),
            output=Path(os.getenv("KAIZEN_OUTPUT", "output")),
        )

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class LocatedFile:
    path: Path | None
    source: str


def locate(expected_file: str, local_dir: Path, fallback_dir: Path) -> LocatedFile:
    """Prefer the local file and use a read-only fallback when it is absent."""
    local = local_dir / expected_file
    if local.is_file():
        return LocatedFile(local, "local")
    fallback = fallback_dir / expected_file
    if fallback.is_file():
        return LocatedFile(fallback, "fallback")
    return LocatedFile(None, "missing")

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

from khm_analyzer.enums import Edition, Volume

if TYPE_CHECKING:
    from collections.abc import Callable


def parse_to_path(text: str) -> Path:
    return Path(text.strip())


def parse_to_edition(n: str) -> Edition:
    return Edition(int(n))


def parse_to_volume(n: str) -> Volume:
    return Volume(int(n))


def parse_rest_of_line(s: str) -> str:
    return s.strip()


MATCHING_TYPES: dict[str, Callable[[str], Any]] = dict(
    Path=parse_to_path,
    Edition=parse_to_edition,
    Volume=parse_to_volume,
    Rest=parse_rest_of_line,
)

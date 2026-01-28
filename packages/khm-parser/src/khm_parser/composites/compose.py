from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

    from khm_parser.bases import CompositeBase


def compose[ResultT, PartT](typ: type[CompositeBase[ResultT]], parts: Iterable[PartT]) -> ResultT:
    parts_list = list()
    for part in parts:
        parts_list.append(part)
        if part.is_the_final_part:
            yield typ(*parts)
            parts_list.clear()

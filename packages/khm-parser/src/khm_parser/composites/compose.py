from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

    from khm_parser.bases import CompositeBase


def compose[ResultT, PartT](typ: type[CompositeBase[ResultT]], parts: Iterable[PartT]) -> ResultT:
    parts_list = list()

    for part in parts:
        composite_yielded_naturally = False
        parts_list.append(part)
        if part.is_the_final_part:
            composite_yielded_naturally = True
            yield typ(*parts_list)
            parts_list.clear()

    if not composite_yielded_naturally:
        yield typ(*parts_list)

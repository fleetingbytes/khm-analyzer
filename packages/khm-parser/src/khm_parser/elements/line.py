from __future__ import annotations

from typing import TYPE_CHECKING

from khm_parser.bases import LineBase
from khm_parser.namespace import NAMESPACE_MAP

if TYPE_CHECKING:
    from collections.abc import Iterable

    from khm_parser.composites import Sentence


class Line(LineBase):
    @property
    def sentences(self) -> Iterable[Sentence]:
        xpath = ".//ns:s[not(ancestor::ns:lg)] | .//ns:lg"
        yield from self.xpath(xpath, namespaces=NAMESPACE_MAP)

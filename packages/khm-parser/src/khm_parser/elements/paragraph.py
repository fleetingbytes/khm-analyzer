from __future__ import annotations

from typing import TYPE_CHECKING

from khm_parser.bases import ParagraphBase
from khm_parser.composites.compose import compose
from khm_parser.composites.sentence import Sentence
from khm_parser.namespace import NAMESPACE_MAP

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable

    from khm_parser.elements.linegroup import LineGroup
    from khm_parser.elements.sentence_part import SentencePart


class Paragraph(ParagraphBase):
    @property
    def sentences_and_linegroups(self) -> Iterable[Sentence | LineGroup]:
        xpath = ".//ns:s[not(ancestor::ns:lg)] | .//ns:lg"
        yield from self.xpath(xpath, namespaces=NAMESPACE_MAP)

    @property
    def sentences(self) -> Generator[Sentence]:
        yield from compose(Sentence, self.sentence_parts)

    @property
    def sentence_parts(self) -> Iterable[SentencePart]:
        xpath = ".//ns:s"
        yield from self.xpath(xpath, namespaces=NAMESPACE_MAP)

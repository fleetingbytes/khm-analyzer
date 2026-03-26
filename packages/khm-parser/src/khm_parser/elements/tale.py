from __future__ import annotations

from typing import TYPE_CHECKING

from khm_parser.bases import HeadBase, ParagraphBase, TaleBase
from khm_parser.composites import Sentence
from khm_parser.composites.compose import compose
from khm_parser.namespace import NAMESPACE_MAP

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable

    from khm_parser.elements import Head, Paragraph, WordPart
    from khm_parser.elements.sentence_part import SentencePart


class Tale(TaleBase):
    @property
    def head(self) -> Head:
        return next(self.iter(tag=HeadBase.TAG))

    @property
    def paragraphs(self) -> Generator[Paragraph]:
        yield from self.iter(tag=ParagraphBase.TAG)

    @property
    def number(self) -> WordPart:
        return self.head.number

    @property
    def title(self) -> Generator[Sentence]:
        yield from self.head.title

    @property
    def sentences(self) -> Generator[Sentence]:
        yield from compose(Sentence, self.sentence_parts)

    @property
    def sentence_parts(self) -> Iterable[SentencePart]:
        xpath = ".//ns:s"
        yield from self.xpath(xpath, namespaces=NAMESPACE_MAP)

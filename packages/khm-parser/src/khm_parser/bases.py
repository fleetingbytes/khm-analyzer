from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar

from lxml import etree

from khm_parser.contracts import (
    AbstractHead,
    AbstractLine,
    AbstractLineGroup,
    AbstractParagraph,
    AbstractSentencePart,
    AbstractTale,
    AbstractWordPart,
)
from khm_parser.namespace import any_namespace, xml_namespace

if TYPE_CHECKING:
    from collections.abc import Iterable
    from io import StringIO


class PrettyPrintMixin:
    def prettyprint(self, **kwargs) -> None:
        xml = etree.tostring(self, pretty_print=True, encoding="unicode", **kwargs)
        print(xml, end="")


class XmlIdMixin:
    @property
    def xmlid(self) -> str:
        xml_id = self.get(xml_namespace("id"), "")
        return xml_id


class HasSentencesMixin:
    @property
    def sentences(self) -> Iterable[SentencePartBase]:
        yield from self.iterdescendants(tag=SentencePartBase.TAG)

    @classmethod
    def add_space_after_sentence(
        cls, sentence: SentencePartBase, separator: str, buffer: StringIO
    ) -> StringIO:
        if not sentence.has_a_following_part:
            buffer.write(separator)
        return buffer


class HasTrailingSpaceMixin:
    @classmethod
    def strip_trailing_space(
        cls, start_of_trailing_space_after_last_element: int, buffer: StringIO
    ) -> StringIO:
        buffer.seek(start_of_trailing_space_after_last_element)
        buffer.truncate()
        return buffer

    @classmethod
    def write_element(
        cls,
        element: SentencePartBase | LineGroupBase | LineBase,
        sentence_separator: str,
        buffer: StringIO,
    ) -> int:
        buffer.write(element.render(sentence_separator=sentence_separator))
        cookie = buffer.tell()
        return cookie


class KhmElement(PrettyPrintMixin, etree.ElementBase, ABC):
    TAG: ClassVar[str] = abstractmethod(lambda cls: NotImplementedError)


class TaleBase(KhmElement, AbstractTale):
    TAG = any_namespace("div")


class HeadBase(KhmElement, AbstractHead):
    TAG = any_namespace("head")


class ParagraphBase(KhmElement, HasSentencesMixin, HasTrailingSpaceMixin, AbstractParagraph):
    TAG = any_namespace("p")


class LineGroupBase(KhmElement, HasTrailingSpaceMixin, AbstractLineGroup):
    TAG = any_namespace("lg")


class LineBase(KhmElement, HasSentencesMixin, AbstractLine):
    TAG = any_namespace("l")


class CompositeBase[PartT](KhmElement):
    def __init__(self, *args: PartT) -> None:
        self._parts: tuple[PartT, ...] = tuple(args)

    @property
    def parts(self) -> Iterable[PartT]:
        return self._parts


class SentenceBase(CompositeBase["SentencePart"]): ...


class SentencePartBase(KhmElement, XmlIdMixin, AbstractSentencePart):
    TAG = any_namespace("s")


class WordBase(CompositeBase["WordPart"]): ...


class WordPartBase(KhmElement, XmlIdMixin, AbstractWordPart):
    TAG = any_namespace("w")

    @property
    @abstractmethod
    def is_the_final_part(self) -> bool: ...

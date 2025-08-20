from __future__ import annotations
from .contracts import AbstractTale, AbstractTitle, AbstractParagraph, AbstractLineGroup, AbstractLine, AbstractSentencePart, AbstractWordPart, Renderable
from lxml import etree
from abc import abstractmethod
from collections.abc import Iterable
from .namespace import any_namespace, xml_namespace
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

    def add_space_after_sentence(self, sentence: SentencePartBase, separator: str, buffer: StringIO) -> StringIO:
        if not sentence.has_a_following_part:
            buffer.write(separator)
        return buffer


class HasTrailingSpaceMixin:
    def strip_trailing_space(self, start_of_trailing_space_after_last_element: int, buffer: StringIO) -> StringIO:
        buffer.seek(start_of_trailing_space_after_last_element)
        buffer.truncate()
        return buffer

    def write_element(self, element: SentencePartBase | LineGroupBase | LineBase, sentence_separator: str, buffer: StringIO) -> int:
        buffer.write(element.render(sentence_separator=sentence_separator))
        cookie = buffer.tell()
        return cookie


class KHMElement(PrettyPrintMixin, etree.ElementBase):
    @property
    @abstractmethod
    def TAG(cls):
        ...


class TaleBase(KHMElement, AbstractTale):
    TAG = any_namespace("div")


class TitleBase(KHMElement, AbstractTitle):
    TAG = any_namespace("head")


class ParagraphBase(KHMElement, HasSentencesMixin, HasTrailingSpaceMixin, AbstractParagraph):
    TAG = any_namespace("p")


class LineGroupBase(KHMElement, HasTrailingSpaceMixin, AbstractLineGroup):
    TAG = any_namespace("lg")


class LineBase(KHMElement, HasSentencesMixin, AbstractLine):
    TAG = any_namespace("l")


class SentencePartBase(KHMElement, XmlIdMixin, AbstractSentencePart):
    TAG = any_namespace("s")


class WordBase(Renderable):
        ...


class WordPartBase(KHMElement, XmlIdMixin, AbstractWordPart):
    TAG = any_namespace("w")

    @property
    @abstractmethod
    def is_the_final_part(self) -> bool:
        ...

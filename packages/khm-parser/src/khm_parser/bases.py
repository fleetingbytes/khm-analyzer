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


class CompositeBase[PartT]:
    def __init__(self, *args: PartT) -> None:
        self._parts: tuple[PartT, ...] = tuple(args)

    @property
    def parts(self) -> Iterable[PartT]:
        return self._parts

    def __len__(self) -> int:
        return len(self.parts)


class SentenceBase(CompositeBase["SentencePart"]): ...


class WordBase(CompositeBase["WordPart"]): ...


class PrettyPrintMixin:
    def prettyprint(self, **kwargs) -> None:
        xml = etree.tostring(self, pretty_print=True, encoding="unicode", **kwargs)
        print(xml, end="")


class XmlIdMixin:
    @property
    def xmlid(self) -> str:
        xml_id = self.get(xml_namespace("id"), "")
        return xml_id


class KhmElement(PrettyPrintMixin, etree.ElementBase, ABC):
    TAG: ClassVar[str] = abstractmethod(lambda cls: NotImplementedError)


class TaleBase(KhmElement, AbstractTale):
    TAG = any_namespace("div")


class HeadBase(KhmElement, AbstractHead):
    TAG = any_namespace("head")


class ParagraphBase(KhmElement, AbstractParagraph):
    TAG = any_namespace("p")


class LineGroupBase(KhmElement, AbstractLineGroup):
    TAG = any_namespace("lg")


class LineBase(KhmElement, AbstractLine):
    TAG = any_namespace("l")


class SentencePartBase(KhmElement, XmlIdMixin, AbstractSentencePart):
    TAG = any_namespace("s")


class WordPartBase(KhmElement, XmlIdMixin, AbstractWordPart):
    TAG = any_namespace("w")

    @property
    @abstractmethod
    def is_the_final_part(self) -> bool: ...

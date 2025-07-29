from .contracts import AbstractTale, AbstractHead, AbstractParagraph, AbstractSentence, AbstractWord
from lxml import etree
from abc import abstractmethod
from .namespace import any_namespace


class KHMElement(etree.ElementBase):
    @property
    @abstractmethod
    def TAG(cls):
        ...

    def prettyprint(self, **kwargs) -> None:
        xml = etree.tostring(self, pretty_print=True, encoding="unicode", **kwargs)
        print(xml, end="")


class TaleBase(KHMElement, AbstractTale):
    TAG = any_namespace("div")


class HeadBase(KHMElement, AbstractHead):
    TAG = any_namespace("head")


class ParagraphBase(KHMElement, AbstractParagraph):
    TAG = any_namespace("p")


class SentenceBase(KHMElement, AbstractSentence):
    TAG = any_namespace("s")


class WordBase(KHMElement, AbstractWord):
    TAG = any_namespace("w")

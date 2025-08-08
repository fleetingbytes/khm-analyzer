from .contracts import AbstractTale, AbstractTitle, AbstractParagraph, AbstractSentence, AbstractWord
from .namespace import xml_namespace
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


class HasXmlId:
    @property
    def xmlid(self) -> str:
        xml_id = self.get(xml_namespace("id"), "")
        return xml_id


class TaleBase(KHMElement, AbstractTale):
    TAG = any_namespace("div")


class TitleBase(KHMElement, AbstractTitle):
    TAG = any_namespace("head")


class ParagraphBase(KHMElement, AbstractParagraph):
    TAG = any_namespace("p")


class SentenceBase(KHMElement, HasXmlId, AbstractSentence):
    TAG = any_namespace("s")


class WordBase(KHMElement, HasXmlId, AbstractWord):
    TAG = any_namespace("w")

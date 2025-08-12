from .contracts import AbstractTale, AbstractTitle, AbstractParagraph, AbstractLineGroup, AbstractLine, AbstractSentence, AbstractWord
from lxml import etree
from abc import abstractmethod
from .namespace import any_namespace
from io import StringIO


class KHMElement(etree.ElementBase):
    @property
    @abstractmethod
    def TAG(cls):
        ...


class TaleBase(KHMElement, AbstractTale):
    TAG = any_namespace("div")


class TitleBase(KHMElement, AbstractTitle):
    TAG = any_namespace("head")


class ParagraphBase(KHMElement, AbstractParagraph):
    TAG = any_namespace("p")


class LineGroupBase(KHMElement, AbstractLineGroup):
    TAG = any_namespace("lg")


class LineBase(KHMElement, AbstractLine):
    TAG = any_namespace("l")


class SentenceBase(KHMElement, AbstractSentence):
    TAG = any_namespace("s")


class WordBase(KHMElement, AbstractWord):
    TAG = any_namespace("w")

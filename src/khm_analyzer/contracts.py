from __future__ import annotations
from .namespace import xml_namespace
from io import StringIO
from abc import ABC, abstractmethod
from collections.abc import Iterable


class PrettyPrintMixin:
    def prettyprint(self, **kwargs) -> None:
        xml = etree.tostring(self, pretty_print=True, encoding="unicode", **kwargs)
        print(xml, end="")

class XmlIdMixin:
    @property
    def xmlid(self) -> str:
        xml_id = self.get(xml_namespace("id"), "")
        return xml_id

class AbstractKHM(ABC):
    pass

class Renderable(PrettyPrintMixin, AbstractKHM):
    @abstractmethod
    def render(self) -> str:
        ...

class Splittable(AbstractKHM):
    @property
    @abstractmethod
    def has_a_following_part(self) -> bool:
        ...

class HasSentences(AbstractKHM):
    def add_space_after_sentence(self, sentence: AbstractSentence, separator: str, buffer: StringIO) -> StringIO:
        if not sentence.has_a_following_part:
            buffer.write(separator)
        return buffer

class HasTrailingSpace(AbstractKHM):
    def strip_trailing_space(self, start_of_trailing_space_after_last_element, buffer: StringIO) -> StringIO:
        buffer.seek(start_of_trailing_space_after_last_element)
        buffer.truncate()
        return buffer


class AbstractTale(Renderable):
    @abstractmethod
    def metadata(self, number: bool, title: bool) -> str:
        ...

    @abstractmethod
    def render(self, number: bool, title: bool, one_sentence_per_line: bool) -> str:
        ...

class AbstractTitle(Renderable):
    @property
    @abstractmethod
    def number(self):
        ...

class AbstractParagraph(Renderable, HasSentences, HasTrailingSpace):
    @abstractmethod
    def render(self, sentence_separator: str) -> str:
        ...

class AbstractLineGroup(Renderable, HasTrailingSpace):
    @property
    @abstractmethod
    def lines(self) -> Iterable[AbstractLine]:
        ...

class AbstractLine(Renderable, HasSentences):
    ...

class AbstractSentence(XmlIdMixin, Renderable, Splittable):
    @property
    @abstractmethod
    def words(self) -> Iterable[AbstractWord]:
        ...

class AbstractWord(XmlIdMixin, Renderable, Splittable):
    @property
    @abstractmethod
    def is_a_part_before_page_break(self) -> bool:
        ...

    @property
    @abstractmethod
    def is_last_in_sentence(self) -> bool:
        ...

    @property
    @abstractmethod
    def is_nth_part(self) -> bool:
        ...

    @property
    @abstractmethod
    def joins_word_right(self) -> bool:
        ...

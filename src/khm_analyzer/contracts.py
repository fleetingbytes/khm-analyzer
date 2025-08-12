from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterable


class AbstractKHM(ABC):
    pass

class Renderable(AbstractKHM):
    @abstractmethod
    def render(self) -> str:
        ...

class Splittable(AbstractKHM):
    @property
    @abstractmethod
    def has_a_following_part(self) -> bool:
        ...


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

class AbstractParagraph(Renderable):
    @abstractmethod
    def render(self, sentence_separator: str) -> str:
        ...

class AbstractLineGroup(Renderable):
    @property
    @abstractmethod
    def lines(self) -> Iterable[AbstractLine]:
        ...

class AbstractLine(Renderable):
    ...

class AbstractSentence(Renderable, Splittable):
    @property
    @abstractmethod
    def words(self) -> Iterable[AbstractWord]:
        ...

class AbstractWord(Renderable, Splittable):
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

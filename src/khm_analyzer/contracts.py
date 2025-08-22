from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterable


class AbstractKHM(ABC):
    pass


class Renderable(AbstractKHM):
    @abstractmethod
    def render(self, **kwargs) -> str: ...


class Splittable(AbstractKHM):
    @property
    @abstractmethod
    def has_a_following_part(self) -> bool: ...


class AbstractTale(Renderable):
    @abstractmethod
    def metadata(self, **kwargs) -> str: ...


class AbstractTitle(Renderable):
    @property
    @abstractmethod
    def number(self): ...


class AbstractParagraph(Renderable): ...


class AbstractLineGroup(Renderable):
    @property
    @abstractmethod
    def lines(self) -> Iterable[AbstractLine]: ...


class AbstractLine(Renderable): ...


class AbstractSentencePart(Renderable, Splittable):
    @property
    @abstractmethod
    def words(self) -> Iterable[Renderable]: ...


class AbstractWordPart(Renderable, Splittable):
    @property
    @abstractmethod
    def is_a_part_before_page_break(self) -> bool: ...

    @property
    @abstractmethod
    def is_last_in_sentencepart(self) -> bool: ...

    @property
    @abstractmethod
    def is_nth_part(self) -> bool: ...

    @property
    @abstractmethod
    def joins_word_right(self) -> bool: ...

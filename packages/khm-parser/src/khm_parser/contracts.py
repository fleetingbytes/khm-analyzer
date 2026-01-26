from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

    from khm_parser.composites.sentence import Sentence
    from khm_parser.composites.word import Word
    from khm_parser.elements.line import Line
    from khm_parser.elements.linegroup import LineGroup


class CompositePart(ABC):
    @property
    @abstractmethod
    def has_a_following_part(self) -> bool: ...

    @property
    @abstractmethod
    def is_the_final_part(self) -> bool: ...


class AbstractTale(ABC):
    @abstractmethod
    def metadata(self, **kwargs) -> str: ...


class AbstractHead(ABC):
    @property
    @abstractmethod
    def number(self): ...


class AbstractParagraph:
    @property
    @abstractmethod
    def sentences_and_linegroups(self) -> Iterable[Sentence | LineGroup]: ...


class AbstractLineGroup(ABC):
    @property
    @abstractmethod
    def lines(self) -> Iterable[Line]: ...


class AbstractLine: ...


class AbstractSentencePart(CompositePart):
    @property
    @abstractmethod
    def words(self) -> Iterable[Word]: ...


class AbstractWordPart(CompositePart):
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

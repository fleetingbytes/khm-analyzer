from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator

    from khm_parser.composites.sentence import Sentence
    from khm_parser.composites.word import Word
    from khm_parser.elements.head import Head
    from khm_parser.elements.line import Line
    from khm_parser.elements.linegroup import LineGroup
    from khm_parser.elements.paragraph import Paragraph


class CompositePart(ABC, Iterable):
    @property
    @abstractmethod
    def has_a_following_part(self) -> bool: ...

    @property
    @abstractmethod
    def is_the_final_part(self) -> bool: ...


class AbstractTale(ABC, Iterable):
    @property
    @abstractmethod
    def head(self) -> Head: ...

    @property
    @abstractmethod
    def paragraphs(self) -> Generator[Paragraph]: ...

    @property
    @abstractmethod
    def number(self) -> int: ...

    @property
    @abstractmethod
    def title(self) -> Generator[Sentence]: ...

    @property
    @abstractmethod
    def sentences(self) -> Generator[Sentence]: ...


class AbstractHead(ABC):
    @property
    @abstractmethod
    def number(self) -> Word: ...

    @property
    @abstractmethod
    def title(self) -> Generator[Sentence]: ...


class AbstractParagraph(ABC, Iterable):
    @property
    @abstractmethod
    def sentences_and_linegroups(self) -> Generator[Sentence | LineGroup]: ...

    @property
    @abstractmethod
    def sentences(self) -> Generator[Sentence]: ...


class AbstractLineGroup(ABC, Iterable):
    @property
    @abstractmethod
    def lines(self) -> Generator[Line]: ...


class AbstractLine(Iterable): ...


class AbstractSentencePart(CompositePart, Iterable):
    @property
    @abstractmethod
    def words(self) -> Generator[Word]: ...


class AbstractWordPart(CompositePart):
    @property
    @abstractmethod
    def is_last_in_sentencepart(self) -> bool: ...

    @property
    @abstractmethod
    def is_nth_part(self) -> bool: ...

    @property
    @abstractmethod
    def joins_word_right(self) -> bool: ...

    @property
    @abstractmethod
    def is_the_final_part(self) -> bool: ...

    @property
    @abstractmethod
    def normalized_transcription(self) -> str: ...

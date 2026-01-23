from __future__ import annotations

from typing import TYPE_CHECKING

from ..bases import TitleBase
from ..composites import Sentence
from ..separators import (
    DEFAULT_SENTENCE_PART_SEPARATOR,
    DEFAULT_WORD_PART_SEPARATOR,
    DEFAULT_WORD_SEPARATOR,
)
from .sentence_part import SentencePart

if TYPE_CHECKING:
    from collections.abc import Generator


class Title(TitleBase):
    @property
    def sentence_parts(self) -> list[SentencePart]:
        result = list(self.iterdescendants(tag=SentencePart.TAG))
        return result

    @property
    def title_sentence_parts(self) -> list[SentencePart]:
        first_sentence_part_is_a_number = bool(self.number)
        result: list[SentencePart] = (
            self.sentence_parts[1:] if first_sentence_part_is_a_number else self.sentence_parts
        )
        return result

    @property
    def sentences(self) -> Generator[Sentence]:
        parts = list()
        for sentence_part in self.sentence_parts:
            parts.append(sentence_part)
            if sentence_part.is_the_final_part:
                yield Sentence(*parts)
                parts.clear()

    @property
    def number(self) -> int | None:
        first_sentence_part = next(iter(self.sentence_parts))
        try:
            first_word = next(iter(first_sentence_part.words)).render()
            first_word_without_trailing_full_stop = first_word.removesuffix(".")
            tale_number = int(first_word_without_trailing_full_stop)
            return tale_number
        except TypeError:
            return None

    def render(
        self,
        sentence_part_separator: str | None = None,
        word_separator: str | None = None,
        word_part_separator: str | None = None,
    ) -> str:
        sentence_part_separator = (
            sentence_part_separator
            if sentence_part_separator is not None
            else DEFAULT_SENTENCE_PART_SEPARATOR
        )
        word_separator = word_separator if word_separator is not None else DEFAULT_WORD_SEPARATOR
        word_part_separator = (
            word_part_separator if word_part_separator is not None else DEFAULT_WORD_PART_SEPARATOR
        )

        sentence = Sentence(*self.title_sentence_parts)
        return sentence.render(
            sentence_part_separator=sentence_part_separator,
            word_separator=word_separator,
            word_part_separator=word_part_separator,
        )

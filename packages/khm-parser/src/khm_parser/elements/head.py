from __future__ import annotations

from typing import TYPE_CHECKING

from khm_parser.bases import HeadBase
from khm_parser.composites import Sentence
from khm_parser.elements.sentence_part import SentencePart

if TYPE_CHECKING:
    from collections.abc import Generator


class Head(HeadBase):
    @property
    def sentence_parts(self) -> list[SentencePart]:
        result: list[SentencePart] = list(self.iterdescendants(tag=SentencePart.TAG))
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

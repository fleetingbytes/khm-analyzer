from __future__ import annotations

from typing import TYPE_CHECKING

from khm_parser.bases import HeadBase
from khm_parser.composites import Sentence, Word, compose
from khm_parser.elements.sentence_part import SentencePart

if TYPE_CHECKING:
    from collections.abc import Generator

    from khm_parser.elements.word_part import WordPart


class Head(HeadBase):
    @property
    def number(self) -> WordPart:
        first_sentence_part: SentencePart = next(iter(self.sentence_parts))
        first_word: Word = next(iter(first_sentence_part.words))
        first_word_part: WordPart = next(iter(first_word.parts))
        return first_word_part

    @property
    def sentence_parts(self) -> list[SentencePart]:
        result: list[SentencePart] = list(self.iterdescendants(tag=SentencePart.TAG))
        return result

    @property
    def title(self) -> Generator[Sentence]:
        yield from compose(Sentence, self.title_sentence_parts)

    @property
    def title_sentence_parts(self) -> list[SentencePart]:
        result: list[SentencePart] = (
            self.sentence_parts[1:] if self.first_sentence_part_is_a_number else self.sentence_parts
        )
        return result

    def first_sentence_part_is_a_number(self) -> bool:
        first_sentence_part = next(iter(self.sentence_parts))
        first_word = next(first_sentence_part.words)
        first_word_part = next(iter(first_word.parts))
        maybe_number: str = first_word_part.normalized_transcription.removesuffix(".")
        try:
            _ = int(maybe_number)
            return True
        except TypeError:
            return False

from __future__ import annotations

from typing import TYPE_CHECKING

from khm_parser.bases import SentencePartBase, WordPartBase
from khm_parser.composites import Word, compose

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable


class SentencePart(SentencePartBase):
    @property
    def word_parts(self) -> Iterable[WordPartBase]:
        yield from self.iterdescendants(tag=WordPartBase.TAG)

    @property
    def words(self) -> Generator[Word]:
        yield from compose(Word, self.word_parts)

    @property
    def is_the_final_part(self) -> bool:
        return not self.has_a_following_part

    @property
    def has_a_following_part(self) -> bool:
        following_part = self.get("next", None)
        return bool(following_part)

    @property
    def last_word(self) -> Word:
        return next(reversed(tuple(self.words)))

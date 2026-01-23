from __future__ import annotations

from io import StringIO
from typing import TYPE_CHECKING

from ..bases import SentencePartBase, WordPartBase
from ..composites import Word
from ..corrections import CorrectionId, corrections
from ..separators import DEFAULT_WORD_SEPARATOR

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable


class SentencePart(SentencePartBase):
    @property
    def word_parts(self) -> Iterable[WordPartBase]:
        yield from self.iterdescendants(tag=WordPartBase.TAG)

    @property
    def words(self) -> Generator[Word]:
        parts = list()
        for word_part in self.word_parts:
            parts.append(word_part)
            if word_part.is_the_final_part:
                yield Word(*parts)
                parts.clear()

    @property
    def is_the_final_part(self) -> bool:
        return not self.has_a_following_part

    @property
    def has_a_following_part(self) -> bool:
        following_part = self.get("next", None)
        return bool(following_part)

    @property
    def correction_id(self) -> CorrectionId:
        return CorrectionId(self.DTAID, self.xmlid)

    def make_arbitrary_correction(self, buffer: StringIO) -> StringIO:
        correction_function = corrections.get(self.correction_id)
        if correction_function:
            buffer = correction_function(buffer)
        return buffer

    def render(self, word_separator: str | None = None, **kwargs) -> str:
        if word_separator is None:
            word_separator = DEFAULT_WORD_SEPARATOR

        buffer = StringIO(word_separator.join(map(lambda word: word.render(**kwargs), self.words)))

        corrected_buffer = self.make_arbitrary_correction(buffer)

        return corrected_buffer.getvalue()

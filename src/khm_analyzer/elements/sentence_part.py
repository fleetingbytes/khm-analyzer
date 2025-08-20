from ..bases import SentencePartBase, WordPartBase, WordBase
from ..composites import Word
from ..corrections import corrections, CorrectionId
from collections.abc import Iterable
from io import StringIO
from itertools import pairwise


class SentencePart(SentencePartBase):
    @property
    def word_parts(self) -> Iterable[WordPartBase]:
        yield from self.iterdescendants(tag=WordPartBase.TAG)

    @property
    def words(self) -> Iterable[WordBase]:
        parts = list()
        for word_part in self.word_parts:
            parts.append(word_part)
            if word_part.is_the_final_part:
                yield Word(*parts)
                parts.clear()

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

    def render(self, word_separator: str=" ", **kwargs) -> str:
        buffer = StringIO()

        for word, next_word in pairwise(self.words):
            buffer.write(word.render())
            if next_word:
                buffer.write(word_separator)

        corrected_buffer = self.make_arbitrary_correction(buffer)

        return corrected_buffer.getvalue()

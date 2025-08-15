from ..bases import SentencePartBase, WordPartBase
from ..corrections import corrections, CorrectionId
from collections.abc import Iterable
from io import StringIO


class SentencePart(SentencePartBase):
    @property
    def words(self) -> Iterable[WordPartBase]:
        yield from self.iterdescendants(tag=WordPartBase.TAG)

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

    def render(self, **kwargs) -> str:
        buffer = StringIO()

        for word in self.words:
            if not word.is_nth_part:
                buffer.write(word.render())
                if all((
                        not word.joins_word_right,
                        not word.is_last_in_sentence,
                        not word.has_a_following_part,
                )):
                    buffer.write(" ")
            if word.is_a_part_before_page_break:
                buffer.write(" ")

        corrected_buffer = self.make_arbitrary_correction(buffer)

        return corrected_buffer.getvalue()

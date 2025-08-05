from ..bases import SentenceBase, WordBase
from collections.abc import Iterable
from io import StringIO


class Sentence(SentenceBase):
    @property
    def words(self) -> Iterable[WordBase]:
        yield from self.iterdescendants(tag=WordBase.TAG)

    def render(self) -> str:
        buffer = StringIO()

        for word in self.words:
            if not word.is_nth_part:
                buffer.write(word.render())
                if all((
                        not word.joins_word_right,
                        not word.is_last_in_sentence,
                )):
                    buffer.write(" ")

        return buffer.getvalue()

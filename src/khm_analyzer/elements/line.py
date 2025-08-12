from ..bases import LineBase, SentenceBase
from collections.abc import Iterable
from io import StringIO


class Line(LineBase):
    def render(self, sentence_separator: str) -> str:
        buffer = StringIO()
        for sentence in self.sentences:
            buffer.write(sentence.render())
            self.add_space_after_sentence(sentence, sentence_separator, buffer)
        return buffer.getvalue()

    @property
    def sentences(self) -> Iterable[SentenceBase]:
        yield from self.iterdescendants(tag=SentenceBase.TAG)

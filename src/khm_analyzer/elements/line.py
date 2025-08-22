from ..bases import LineBase
from io import StringIO


class Line(LineBase):
    def render(self, sentence_separator: str) -> str:
        buffer = StringIO()
        for sentence in self.sentences:
            buffer.write(sentence.render())
            self.add_space_after_sentence(sentence, sentence_separator, buffer)
        return buffer.getvalue()

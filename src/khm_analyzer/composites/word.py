from ..bases import WordBase
from io import StringIO


class Word(WordBase):
    def __init__(self, *args) -> None:
        self.parts = tuple(args)

    def render(self, *args) -> str:
        buffer = StringIO()
        for word_part in self.parts:
            buffer.write(word_part.render())
        return buffer.getvalue()

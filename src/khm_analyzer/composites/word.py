from io import StringIO

from ..bases import WordBase


class Word(WordBase):
    def __init__(self, *args) -> None:
        self.parts = tuple(args)

    def render(self, *args) -> str:
        buffer = StringIO()
        for word_part in self.parts:
            buffer.write(word_part.render())
        return buffer.getvalue()

from ..bases import LineGroupBase, LineBase
from io import StringIO


class LineGroup(LineGroupBase):
    @property
    def lines(self):
        yield from self.iterdescendants(tag=LineBase.TAG)

    def render(self, sentence_separator: str, **kwargs) -> str:
        buffer = StringIO()
        start_of_trailing_space_after_last_line: int = buffer.tell()

        for line in self.lines:
            start_of_trailing_space_after_last_line = self.write_element(line, sentence_separator, buffer)
            buffer = self.add_space_after_line(buffer)

        buffer = self.strip_trailing_space(start_of_trailing_space_after_last_line, buffer)

        return buffer.getvalue()

    def add_space_after_line(self, buffer: StringIO) -> StringIO:
        buffer.write("\n")
        return buffer

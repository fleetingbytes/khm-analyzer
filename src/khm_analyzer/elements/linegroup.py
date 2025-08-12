from ..bases import LineGroupBase, LineBase
from io import StringIO


class LineGroup(LineGroupBase):
    @property
    def lines(self):
        yield from self.iterdescendants(tag=LineBase.TAG)

    def render(self) -> str:
        buffer = StringIO()
        for line in self.lines:
            buffer.write(line.render())
        return buffer.getvalue()


from lxml import etree
from collections.abc import Iterable
from ..bases import TaleBase, HeadBase, ParagraphBase
from io import StringIO


class Tale(TaleBase):
    @property
    def head(self) -> HeadBase:
        return next(self.iter(tag=HeadBase.TAG))

    @property
    def paragraphs(self) -> Iterable[str]:
        yield from self.iter(tag=ParagraphBase.TAG)

    def render(self) -> str:
        buffer = StringIO(self.head.render())
        buffer.write("\n\n")
        paragraphs = "\n\n".join(paragraph.render() for paragraph in self.paragraphs)
        buffer.write(paragraphs)
        return buffer.getvalue()


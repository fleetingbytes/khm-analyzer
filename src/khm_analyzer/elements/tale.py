from lxml import etree
from collections.abc import Iterable
from ..bases import TaleBase, HeadBase, ParagraphBase


class Tale(TaleBase):
    @property
    def head(self) -> HeadBase:
        return next(self.iter(tag=HeadBase.TAG))

    @property
    def paragraphs(self) -> Iterable[str]:
        yield from self.iter(tag=ParagraphBase.TAG)

    def render(self) -> str:
        return "here be tale"

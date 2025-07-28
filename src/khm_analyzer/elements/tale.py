from lxml import etree
from collections.abc import Iterable
from ..bases import TaleBase, HeadBase


class Tale(TaleBase):
    @property
    def head(self) -> Iterable[HeadBase]:
        return next(self.iter(tag="{*}head"))
    @property
    def paragraphs(self) -> Iterable[str]:
        yield from self.iter(tag="{*}p")

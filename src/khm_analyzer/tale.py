from abc import ABC, abstractmethod
from lxml import etree
from collections.abc import Iterable


class TaleBase(ABC):
    @property
    @abstractmethod
    def sentences(self) -> Iterable[str]:
        ...


class Tale(etree.ElementBase, TaleBase):
    def prettyprint(self, **kwargs) -> None:
        xml = etree.tostring(self, pretty_print=True, **kwargs)
        print(xml.decode(), end="")
    @property
    def raw_head(self) -> Iterable[etree.Element]:
        yield from self.iter(tag="{*}head")
    @property
    def raw_paragraphs(self) -> Iterable[etree.Element]:
        yield from self.iter(tag="{*}p")
    @property
    def raw_sentences(self):
        yield from self.iter(tag="{*}s")
    @property
    def head(self) -> Iterable[str]:
        return next(self.raw_head)
    @property
    def sentences(self) -> Iterable[str]:
        pass

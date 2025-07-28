from .contracts import AbstractTale, AbstractHead
from lxml import etree


class KHMElement(etree.ElementBase):
    def prettyprint(self, **kwargs) -> None:
        xml = etree.tostring(self, pretty_print=True, encoding="unicode", **kwargs)
        print(xml, end="")
    pass


class TaleBase(KHMElement, AbstractTale):
    pass


class HeadBase(KHMElement, AbstractHead):
    pass

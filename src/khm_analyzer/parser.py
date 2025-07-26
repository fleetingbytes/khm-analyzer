from lxml import etree
from io import TextIOWrapper
from collections.abc import Mapping


NAMESPACE_MAP = { "ns": "http://www.tei-c.org/ns/1.0" }

def parse(fd: TextIOWrapper) -> etree.Element:
    tree = etree.parse(fd)
    root = tree.getroot()
    return root

def get_fairy_tale(root: etree.Element, n: int) -> etree.Element | None:
    xpath = f".//ns:div[ns:head//ns:w[@lemma='{n}.']]"
    results = root.xpath(xpath, namespaces=NAMESPACE_MAP)
    return next(iter(results)) if results else None

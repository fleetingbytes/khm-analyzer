from lxml import etree
from io import TextIOWrapper
from collections.abc import Mapping
from .tale import Tale


NAMESPACE_MAP = { "ns": "http://www.tei-c.org/ns/1.0" }

def parse(fd: TextIOWrapper) -> etree.Element:
    parser = etree.XMLParser()
    lookup = etree.ElementDefaultClassLookup(element=Tale)
    parser.set_element_class_lookup(lookup)

    tree = etree.parse(fd, parser)
    root = tree.getroot()
    return root

def get_fairy_tale(root: etree.Element, n: int) -> etree.Element | None:
    xpath = f".//ns:div[ns:head//ns:w[@lemma='{n}.']]"
    results = root.xpath(xpath, namespaces=NAMESPACE_MAP)
    tale = next(iter(results)) if results else None
    return tale

from lxml import etree
from io import TextIOWrapper
from .lookup import Lookup
from .namespace import NAMESPACE_MAP


def parse(fd: TextIOWrapper) -> etree.Element:
    parser = etree.XMLParser()
    parser.set_element_class_lookup(Lookup())

    tree = etree.parse(fd, parser)
    root = tree.getroot()
    return root

def get_fairy_tale(root: etree.Element, n: int) -> etree.Element | None:
    xpath = f".//ns:div[ns:head//ns:w[@lemma='{n}.']]"
    results = root.xpath(xpath, namespaces=NAMESPACE_MAP)
    tale = next(iter(results)) if results else None
    return tale

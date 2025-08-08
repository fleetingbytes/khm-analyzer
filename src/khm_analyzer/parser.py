from lxml import etree
from io import TextIOWrapper
from .lookup import Lookup
from .namespace import NAMESPACE_MAP
from .errors import DtaidNotFoundError
import re


DTAID_REGEX = re.compile("""<idno\s+type="DTAID"\s*>(?P<dtaid>\d+)</idno>""")


def go_to_beginning_of_the_file(fd: TextIOWrapper) -> None:
    fd.seek(0)


def get_dtaid(fd: TextIOWrapper) -> int:
    """
    Get the DTAID from the XML file before it is parsed.

    This is much faster than to looking up the document's DTAID
    after parsing from within every element tag which needs it.
    """
    for line in fd:
        if match := DTAID_REGEX.search(line):
            go_to_beginning_of_the_file(fd)
            dtaid = int(match.group("dtaid"))
            return dtaid
    raise DtaidNotFoundError


def parse(fd: TextIOWrapper) -> etree.Element:
    parser = etree.XMLParser()
    dtaid = get_dtaid(fd)
    Lookup.DTAID = dtaid
    parser.set_element_class_lookup(Lookup())

    tree = etree.parse(fd, parser)
    root = tree.getroot()
    return root


def get_fairy_tale(root: etree.Element, n: int) -> etree.Element | None:
    xpath = f".//ns:div[ns:head//ns:w[@lemma='{n}.']]"
    results = root.xpath(xpath, namespaces=NAMESPACE_MAP)
    tale = next(iter(results)) if results else None
    return tale

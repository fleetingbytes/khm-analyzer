from __future__ import annotations

import re
from typing import TYPE_CHECKING

from lxml import etree

from khm_parser.errors import DtaIdNotFoundError
from khm_parser.lookup import Lookup
from khm_parser.namespace import NAMESPACE_MAP
from khm_parser.utils import set_stream_position_to_the_start

if TYPE_CHECKING:
    from io import BufferedReader
    from pathlib import Path

    from khm_parser.elements import Tale

DTAID_REGEX = re.compile(rb"""<idno\s+type="DTAID"\s*>(?P<dtaid>\d+)</idno>""")


def get_dtaid(fd: BufferedReader) -> int:
    """
    Get the DTAID from the XML file before it is parsed.

    This is much faster than looking up the document's DTAID
    after parsing from within every element tag which needs it.
    """
    for line in fd:
        if match := DTAID_REGEX.search(line):
            set_stream_position_to_the_start(fd)
            dtaid = int(match.group("dtaid"))
            return dtaid
    raise DtaIdNotFoundError


def parse(fd: BufferedReader) -> etree.Element:
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


def parse_tale(path: Path, tale_number: int) -> Tale:
    with path.open("rb") as file:
        root: etree.Element = parse(file)
        tale: Tale = get_fairy_tale(root, tale_number)
        return tale

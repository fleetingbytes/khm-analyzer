from __future__ import annotations

import re
from typing import TYPE_CHECKING

from lxml import etree

from khm_parser.errors import DtaIdNotFoundError
from khm_parser.lookup import Lookup
from khm_parser.namespace import NAMESPACE_MAP
from khm_parser.utils import set_stream_position_to_the_start

if TYPE_CHECKING:
    from collections.abc import Generator
    from io import BufferedReader
    from pathlib import Path

    from khm_parser.elements import Tale

DTAID_REGEX = re.compile(rb"""<idno\s+type="DTAID"\s*>(?P<dtaid>\d+)</idno>""")

EXPECTED_NUMBER_OF_KHM_ED1_VOL1_TALE_THIRTY_ONE = 31
ACTUAL_NUMBER_OF_KHM_ED1_VOL1_TALE_THIRTY_ONE = 30
EXPECTED_NUMBER_OF_TALES_NUMBRERED_THIRTY_IN_KHM_ED1_VOL1 = 2


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


def parse_tale(path: Path, tale_number: int) -> Tale:
    with path.open("rb") as file:
        root: etree.Element = parse(file)
        tale: Tale = get_fairy_tale(root, tale_number)
        return tale


def get_fairy_tale(root: etree.Element, n: int) -> Tale | None:
    xpath = f".//ns:div[@n='1' and ns:head//ns:w[@lemma='{n}.']]"
    results = root.xpath(xpath, namespaces=NAMESPACE_MAP)
    tale = next(iter(results)) if results else None

    tale = correct_anomaly_with_khm_ed1_vol1_tale_31(tale, n, root)

    return tale


def correct_anomaly_with_khm_ed1_vol1_tale_31(
    tale: Tale | None, n: int, root: etree.Element
) -> Tale | None:
    """
    khm-ed1-vol1 tale 31 is misnumbered as 30 (even in the xml annotation, true to the misprint),
    so there is two tales with the number 30 and no tale with number 31
    """
    if tale is None and n == EXPECTED_NUMBER_OF_KHM_ED1_VOL1_TALE_THIRTY_ONE:
        xpath = (
            ".//ns:div[@n='1' and "
            f"ns:head//ns:w[@lemma='{ACTUAL_NUMBER_OF_KHM_ED1_VOL1_TALE_THIRTY_ONE}.']]"
        )
        results = root.xpath(xpath, namespaces=NAMESPACE_MAP)
        if results and len(results) == EXPECTED_NUMBER_OF_TALES_NUMBRERED_THIRTY_IN_KHM_ED1_VOL1:
            index_of_tale_31 = EXPECTED_NUMBER_OF_TALES_NUMBRERED_THIRTY_IN_KHM_ED1_VOL1 - 1
            tale = results[index_of_tale_31]

    return tale


def get_all_fairy_tales(path: Path) -> Generator[Tale]:
    with path.open("rb") as file:
        root: etree.Element = parse(file)

    xpath = r".//ns:div[@n='1' and ns:head//ns:w[exslt:test(@lemma, '^\d+\.$')]]"
    tales = root.xpath(xpath, namespaces=NAMESPACE_MAP)

    yield from tales

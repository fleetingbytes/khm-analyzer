from __future__ import annotations

from typing import TYPE_CHECKING

from lxml import etree

if TYPE_CHECKING:
    from io import BytesIO, TextIOWrapper


def check_xml(buffer: TextIOWrapper | BytesIO) -> None:
    try:
        _ = etree.parse(buffer)
    except etree.XMLSyntaxError:
        raise

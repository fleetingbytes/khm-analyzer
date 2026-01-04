from __future__ import annotations

from sys import stderr
from typing import TYPE_CHECKING

from click import Path as ClickPath
from click import echo, open_file
from lxml import etree

from .utils import debug

if TYPE_CHECKING:
    from io import BytesIO, TextIOWrapper


@debug
def validate_paths(paths: list[ClickPath]) -> None:
    for path in paths:
        with open_file(path, mode="r", encoding="UTF-8") as file:
            try:
                check_xml(file)
            except etree.XMLSyntaxError as err:
                echo(path, "is invalid:", err, file=stderr)


def check_xml(buffer: TextIOWrapper | BytesIO) -> None:
    try:
        _ = etree.parse(buffer)
    except etree.XMLSyntaxError:
        raise

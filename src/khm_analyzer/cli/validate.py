from __future__ import annotations

from sys import stderr
from typing import TYPE_CHECKING
from warnings import catch_warnings

from click import echo
from lxml import etree
from readylog.decorators import debug_in

from khm_analyzer.enums import ReturnCode
from khm_analyzer.validation import check_xml

if TYPE_CHECKING:
    from click import File


@debug_in
def validate(files: tuple[File]) -> ReturnCode:
    with catch_warnings(record=True) as w:
        result: ReturnCode = validate_files(files)
    for warning in w:
        echo(warning.message)
    return result


@debug_in
def validate_files(files: tuple[File]) -> ReturnCode:
    result = ReturnCode.OK

    for file in files:
        try:
            check_xml(file)
        except etree.XMLSyntaxError as err:
            echo(f"'{file.name}' is invalid: {err}", file=stderr)
            result = ReturnCode.INVALID_XML

    return result

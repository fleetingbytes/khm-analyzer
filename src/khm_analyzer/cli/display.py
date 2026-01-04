from __future__ import annotations

from typing import TYPE_CHECKING

from click import echo

import khm_analyzer.parser as khm_parser

if TYPE_CHECKING:
    from click import File
    from lxml import etree

    from khm_analyzer.elements import Tale


def display(
    source_file: File,
    tale_number: int,
    include_tale_number: bool,
    include_tale_title: bool,
    one_sentence_per_line: bool,
) -> None:
    root: etree.Element = khm_parser.parse(source_file)
    tale: Tale = khm_parser.get_fairy_tale(root, tale_number)

    kwargs = {
        "number": include_tale_number,
        "title": include_tale_title,
        "one_sentence_per_line": one_sentence_per_line,
    }

    echo(tale.render(**kwargs))

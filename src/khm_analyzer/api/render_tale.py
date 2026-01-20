from __future__ import annotations

from typing import TYPE_CHECKING

import khm_analyzer.parser as khm_parser

if TYPE_CHECKING:
    from click import File
    from lxml import etree

    from khm_analyzer.elements import Tale


def render_tale(source_file: File, tale_number: int, **kwargs) -> str:
    root: etree.Element = khm_parser.parse(source_file)
    tale: Tale = khm_parser.get_fairy_tale(root, tale_number)

    return tale.render(**kwargs)

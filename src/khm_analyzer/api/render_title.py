from __future__ import annotations

from typing import TYPE_CHECKING

import khm_analyzer.parser as khm_parser

from ..separators import (
    DEFAULT_SENTENCE_PART_SEPARATOR,
    DEFAULT_WORD_PART_SEPARATOR,
    DEFAULT_WORD_SEPARATOR,
)

if TYPE_CHECKING:
    from io import BufferedReader

    from lxml import etree

    from khm_analyzer.elements import Tale


def render_title(
    source_file: BufferedReader,
    tale_number: int,
    *,
    show_number: bool = False,
    show_title: bool = False,
    paragraph_separator: str | None = None,
    sentence_separator: str | None = None,
    sentence_part_separator: str | None = None,
    word_separator: str | None = None,
    word_part_separator: str | None = None,
) -> str:
    kwargs = dict(
        sentence_part_separator=(
            sentence_part_separator
            if sentence_part_separator is not None
            else DEFAULT_SENTENCE_PART_SEPARATOR
        ),
        word_separator=word_separator if word_separator is not None else DEFAULT_WORD_SEPARATOR,
        word_part_separator=(
            word_part_separator if word_part_separator is not None else DEFAULT_WORD_PART_SEPARATOR
        ),
    )

    root: etree.Element = khm_parser.parse(source_file)
    tale: Tale = khm_parser.get_fairy_tale(root, tale_number)

    return tale.metadata(show_number=True, show_title=True, **kwargs)

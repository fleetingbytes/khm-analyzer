from __future__ import annotations

from typing import TYPE_CHECKING

from click import echo

if TYPE_CHECKING:
    from io import TextIOWrapper


def display(
    source_file: TextIOWrapper,
    tale_number: int,
    include_tale_number: bool,
    include_tale_title: bool,
    one_sentence_per_line: bool,
) -> None:
    sentence_separator = "\n" if one_sentence_per_line else " "

    _kwargs = {
        "show_number": include_tale_number,
        "show_title": include_tale_title,
        "sentence_separator": sentence_separator,
    }

    text: str = "placeholder"

    echo(text)

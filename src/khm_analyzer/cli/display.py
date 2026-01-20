from __future__ import annotations

from typing import TYPE_CHECKING

from click import echo

from khm_analyzer.api import render_tale

if TYPE_CHECKING:
    from click import File


def display(
    source_file: File,
    tale_number: int,
    include_tale_number: bool,
    include_tale_title: bool,
    one_sentence_per_line: bool,
) -> None:
    kwargs = {
        "number": include_tale_number,
        "title": include_tale_title,
        "one_sentence_per_line": one_sentence_per_line,
    }

    text: str = render_tale(source_file, tale_number, **kwargs)

    echo(text)

from __future__ import annotations

from io import StringIO
from itertools import product
from typing import TYPE_CHECKING

from khm_enums import Edition, Volume
from khm_parser.utils import set_stream_position_to_the_start
from khm_renderer import render_word, render_word_part
from khm_renderer.decorators import inject_default_separators

if TYPE_CHECKING:
    from io import StringIO
    from pathlib import Path

    from khm_parser.elements import Tale
    from khm_renderer.separators import Separators


def check_presence_of_source_files(directory: Path) -> None:
    file_names_with_parent_dir = map(lambda path: path.name, directory.glob("*.xml"))
    file_names = tuple(map(str, file_names_with_parent_dir))

    found_at_least_one_document = False

    for ed, vol in product(Edition, Volume):
        if f"khm-ed{ed.value}-vol{vol.value}.xml" in file_names:
            found_at_least_one_document = True
            break

    assert found_at_least_one_document, f"Cannot find any source documents in {directory.absolute()}"


def get_source_path(directory: Path, edition: Edition, volume: Volume) -> Path:
    path = directory / f"khm-ed{edition.value}-vol{volume.value}.xml"
    return path


def read_string_buffer(buffer: StringIO) -> str:
    set_stream_position_to_the_start(buffer)
    return buffer.read()


def find_and_render_word_part(tale: Tale, word_part_id: str) -> str | None:
    for paragraph in tale:
        for sentence in paragraph:
            for word in sentence.words:
                for word_part in word:
                    if word_part.xmlid == word_part_id:
                        return render_word_part(word_part)


@inject_default_separators
def find_and_render_word(
    tale: Tale, buffer: StringIO, word_id: str, *, sep: Separators | None = None
) -> StringIO:
    for paragraph in tale:
        for sentence in paragraph:
            for word in sentence.words:
                if word.id == word_id:
                    return render_word(word, buffer, sep=sep)

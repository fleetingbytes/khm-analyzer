from __future__ import annotations

from itertools import product
from typing import TYPE_CHECKING

from khm_enums import Edition, Volume
from khm_parser.utils import set_stream_position_to_the_start

if TYPE_CHECKING:
    from io import StringIO
    from pathlib import Path


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

from __future__ import annotations

from itertools import product
from typing import TYPE_CHECKING

from readylog.decorators import debug_in

from khm_cli.download_source import create_parent_dir_if_not_exists
from khm_downloader import get_download_link, get_source_document_as_raw_bytes
from khm_enums import Edition, Volume

if TYPE_CHECKING:
    from pathlib import Path


@debug_in
def download_all_sources(directory: Path):
    pattern = directory / "khm.xml"

    for edition, volume in product(tuple(Edition), tuple(Volume)):
        path = pattern.with_stem(f"{pattern.stem}-ed{edition}-vol{volume}")

        link = get_download_link(edition, volume)
        raw_bytes = get_source_document_as_raw_bytes(link)

        create_parent_dir_if_not_exists(path)

        with path.open("wb") as file:
            file.write(raw_bytes)

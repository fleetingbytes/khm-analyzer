from __future__ import annotations

from typing import TYPE_CHECKING

from click import open_file
from readylog.decorators import debug_in

from khm_analyzer.download import get_download_link, get_source_document_as_raw_bytes

if TYPE_CHECKING:
    from pathlib import Path

    from khm_analyzer.enums import Edition, Volume


@debug_in
def create_parent_dir_if_not_exists(file_path: Path) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)


@debug_in
def download_source(edition: Edition, volume: Volume, file_path: Path) -> None:
    link = get_download_link(edition, volume)
    raw_bytes = get_source_document_as_raw_bytes(link)

    create_parent_dir_if_not_exists(file_path)

    with open_file(file_path, mode="wb") as file:
        file.write(raw_bytes)

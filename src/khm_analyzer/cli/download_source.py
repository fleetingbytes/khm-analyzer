from argparse import Namespace
from pathlib import Path
from ..utils import debug_in
from ..download import get_download_link, get_source_document_as_raw_bytes


def create_parent_dir_if_not_exists(file: Path) -> None:
    file.parent.mkdir(parents=True, exist_ok=True)


@debug_in
def download_source(args: Namespace) -> None:
    edition = args.edition
    volume = args.volume
    output_file = args.file

    link = get_download_link(edition, volume)
    raw_bytes = get_source_document_as_raw_bytes(link)

    create_parent_dir_if_not_exists(output_file)

    with output_file as file:
        file.write(raw_bytes)

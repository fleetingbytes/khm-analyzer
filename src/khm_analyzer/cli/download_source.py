from argparse import Namespace
from ..utils import debug_in
from ..download import get_download_link, get_source_document_as_raw_bytes


@debug_in
def download_source(args: Namespace) -> None:
    edition = args.edition
    volume = args.volume
    output_file = args.file

    link = get_download_link(edition, volume)
    raw_bytes = get_source_document_as_raw_bytes(link)

    with output_file as file:
        file.write(raw_bytes)

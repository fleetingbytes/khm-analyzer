from argparse import Namespace
from ..utils import debug_in
from ..download import get_source_document_as_raw_bytes


@debug_in
def download_source(args: Namespace) -> None:
    edition = args.edition
    volume = args.volume
    output_file = args.file

    raw_bytes = get_source_document_as_raw_bytes(edition, volume)
    with output_file as file:
        file.write(raw_bytes)

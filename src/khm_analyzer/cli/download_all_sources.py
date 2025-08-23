from argparse import Namespace
from itertools import product
from ..download import EDITION_RANGE, VOLUME_RANGE, get_download_link, get_source_document_as_raw_bytes
from ..utils import debug_in


@debug_in
def download_all_sources(args: Namespace):
    pattern = args.path_pattern

    for edition, volume in product(EDITION_RANGE, VOLUME_RANGE):
        path = pattern.with_stem(f"{pattern.stem}-ed{edition}-vol{volume}")

        link = get_download_link(edition, volume)
        raw_bytes = get_source_document_as_raw_bytes(link)

        with path.open("wb") as file:
            file.write(raw_bytes)

import requests
from argparse import Namespace


MAX_EDITION = 7
MAX_VOLUME = 2
EDITION_RANGE = range(1, MAX_EDITION + 1)
VOLUME_RANGE = range(1, MAX_VOLUME + 1)


def download_source(args: Namespace) -> None:
    edition = args.edition
    volume = args.volume
    output_file = args.file

    raw_bytes = get_source_document_as_raw_bytes(edition, volume)
    with output_file as file:
        file.write(raw_bytes)

def get_source_document_as_raw_bytes(edition: int, volume: int) -> bytes:
    url = get_download_link(edition, volume)
    response = requests.get(url)
    assert response.ok, f"Got response {response.status_code}"
    return response.content

def get_download_link(edition: int, volume: int) -> str:
    assert edition in EDITION_RANGE, f"Only edition 1 through {MAX_EDITION} is available"
    assert volume in VOLUME_RANGE , f"Only volume 1 or {MAX_VOLUME} is available"

    link_base = "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen0"
    year = publication_year(edition, volume)

    link = f"{link_base}{volume}_{year}"

    return link


def publication_year(edition: int, volume: int) -> int:
    if edition == 1:
        return edition_one_publication_year(volume)
    else:
        return edition_two_and_later_publication_year(edition)


def edition_one_publication_year(volume: int) -> int:
    if volume == 1:
        return 1812
    else:
        return 1815

def edition_two_and_later_publication_year(edition: int) -> int:
    EDITION_TO_YEAR_MAP = {
        2: 1819,
        3: 1837,
        4: 1840,
        5: 1843,
        6: 1850,
        7: 1857,
    }
    return EDITION_TO_YEAR_MAP[edition]

from khm_enums import Edition, Volume
from requests import Response, get

from khm_downloader.constants import (
    DOWNLOAD_LINK_BASE,
    EDITION_ONE_VOLUME_ONE_PUBLICATION_YEAR,
    EDITION_ONE_VOLUME_TWO_PUBLICATION_YEAR,
    EDITION_TO_PUBLICATION_YEAR_MAP,
)


def get_source_document_as_raw_bytes(url: str) -> bytes:
    response: Response = get(url)
    assert response.ok, f"Got response {response.status_code}"
    return response.content


def get_download_link(edition: Edition, volume: Volume) -> str:
    year = publication_year(edition, volume)
    link = f"{DOWNLOAD_LINK_BASE}{volume}_{year}"
    return link


def publication_year(edition: Edition, volume: Volume) -> int:
    if edition is Edition.ONE:
        return edition_one_publication_year(volume)
    else:
        return edition_two_and_later_publication_year(edition)


def edition_one_publication_year(volume: Volume) -> int:
    if volume is Volume.ONE:
        return EDITION_ONE_VOLUME_ONE_PUBLICATION_YEAR
    else:
        return EDITION_ONE_VOLUME_TWO_PUBLICATION_YEAR


def edition_two_and_later_publication_year(edition: Edition) -> int:
    return EDITION_TO_PUBLICATION_YEAR_MAP[edition]

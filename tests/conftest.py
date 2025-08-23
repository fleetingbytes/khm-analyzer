from pytest import fixture
from os import getenv


def get_source_document_as_raw_bytes(edition: int, volume: int) -> bytes:
    content = getenv(f"KHM_ED{edition}_VOL{volume}", default="")
    return content.encode("UTF-8")


@fixture
def khm_edition_volume(request, pytestconfig):
    """
    Returns KHM source XML as bytes string,
    preferably from pytest cache.
    """
    edition, volume = request.param
    content = get_source_document_as_raw_bytes(edition, volume)
    return content

from pytest import fixture
from base64 import b64encode, b64decode
from khm_analyzer.download import get_source_document_as_raw_bytes


def encode_for_cache(raw: bytes) -> str:
    encoded: bytes = b64encode(raw)
    cacheable: str = encoded.decode("ascii")
    return cacheable


def decode_cache(cacheable: str) -> bytes:
    encoded: bytes = cacheable.encode("ascii")
    decoded: bytes = b64decode(encoded)
    return decoded


def get_new_cacheable_content(edition, volume) -> str:
    uncacheable_raw_content: bytes = get_source_document_as_raw_bytes(edition, volume)
    cacheable_content: str = encode_for_cache(uncacheable_raw_content)
    return cacheable_content


def get_cached_content_or_set_new_cache(pytestconfig, edition: int, volume: int) -> bytes:
    cache_path = f"khm_analyzer/{edition}_{volume}"
    cacheable_content = pytestconfig.cache.get(cache_path, None)
    if cacheable_content is None:
        cacheable_content: str = get_new_cacheable_content(edition, volume)
        pytestconfig.cache.set(cache_path, cacheable_content)
    decoded_cache_content: bytes = decode_cache(cacheable_content)
    return decoded_cache_content


@fixture
def khm_edition_volume(request, pytestconfig):
    """
    Returns KHM source XML as bytes string,
    preferably from pytest cache.
    """
    edition, volume = request.param
    cached = get_cached_content_or_set_new_cache(pytestconfig, edition, volume)
    return cached

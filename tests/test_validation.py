from __future__ import annotations

from io import BytesIO

from pytest import mark, param

from khm_analyzer.download import get_download_link, get_source_document_as_raw_bytes
from khm_analyzer.enums import Edition, Volume
from khm_analyzer.validation import check_xml

from .markers import xml_download


@xml_download
@mark.parametrize(
    "edition, volume, expected_is_valid",
    (
        param(Edition.ONE, Volume.ONE, True, id="ed1-vol1"),
        param(Edition.ONE, Volume.TWO, True, id="ed1-vol2"),
        param(Edition.TWO, Volume.ONE, True, id="ed2-vol1"),
        param(Edition.TWO, Volume.TWO, True, id="ed2-vol2"),
        param(Edition.THREE, Volume.ONE, True, id="ed3-vol1"),
        param(Edition.THREE, Volume.TWO, True, id="ed3-vol2"),
        param(Edition.FOUR, Volume.ONE, True, id="ed4-vol1"),
        param(Edition.FOUR, Volume.TWO, True, id="ed4-vol2"),
        param(Edition.FIVE, Volume.ONE, True, id="ed5-vol1"),
        param(Edition.FIVE, Volume.TWO, True, id="ed5-vol2"),
        param(Edition.SIX, Volume.ONE, True, id="ed6-vol1"),
        param(Edition.SIX, Volume.TWO, True, id="ed6-vol2"),
        param(Edition.SEVEN, Volume.ONE, True, id="ed7-vol1"),
        param(Edition.SEVEN, Volume.TWO, True, id="ed7-vol2"),
    ),
)
def test_source_documents_valid(edition: Edition, volume: Volume, expected_is_valid: bool):
    link: str = get_download_link(edition, volume)
    raw_bytes: bytes = get_source_document_as_raw_bytes(link)
    xml_document = BytesIO(raw_bytes)

    check_xml(xml_document)

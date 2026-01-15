from __future__ import annotations

from pytest import mark, param

from khm_analyzer.download import get_download_link, get_source_document_as_raw_bytes, publication_year
from khm_analyzer.enums import Edition, Volume


@mark.parametrize(
    "edition, volume, expected_year",
    (
        param(Edition.ONE, Volume.ONE, 1812, id="ed1-vol1"),
        param(Edition.ONE, Volume.TWO, 1815, id="ed1-vol2"),
        param(Edition.TWO, Volume.ONE, 1819, id="ed2-vol1"),
        param(Edition.TWO, Volume.TWO, 1819, id="ed2-vol2"),
        param(Edition.THREE, Volume.ONE, 1837, id="ed3-vol1"),
        param(Edition.THREE, Volume.TWO, 1837, id="ed3-vol2"),
        param(Edition.FOUR, Volume.ONE, 1840, id="ed4-vol1"),
        param(Edition.FOUR, Volume.TWO, 1840, id="ed4-vol2"),
        param(Edition.FIVE, Volume.ONE, 1843, id="ed5-vol1"),
        param(Edition.FIVE, Volume.TWO, 1843, id="ed5-vol2"),
        param(Edition.SIX, Volume.ONE, 1850, id="ed6-vol1"),
        param(Edition.SIX, Volume.TWO, 1850, id="ed6-vol2"),
        param(Edition.SEVEN, Volume.ONE, 1857, id="ed7-vol1"),
        param(Edition.SEVEN, Volume.TWO, 1857, id="ed7-vol2"),
    ),
)
def test_publication_year(edition: Edition, volume: Volume, expected_year):
    year = publication_year(edition, volume)
    assert year == expected_year


@mark.parametrize(
    "edition, volume, expected_link",
    (
        param(
            Edition.ONE,
            Volume.ONE,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1812",
            id="ed1-vol1",
        ),
        param(
            Edition.ONE,
            Volume.TWO,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1815",
            id="ed1-vol2",
        ),
        param(
            Edition.TWO,
            Volume.ONE,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1819",
            id="ed2-vol1",
        ),
        param(
            Edition.TWO,
            Volume.TWO,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1819",
            id="ed2-vol2",
        ),
        param(
            Edition.THREE,
            Volume.ONE,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1837",
            id="ed3-vol1",
        ),
        param(
            Edition.THREE,
            Volume.TWO,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1837",
            id="ed3-vol2",
        ),
        param(
            Edition.FOUR,
            Volume.ONE,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1840",
            id="ed4-vol1",
        ),
        param(
            Edition.FOUR,
            Volume.TWO,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1840",
            id="ed4-vol2",
        ),
        param(
            Edition.FIVE,
            Volume.ONE,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1843",
            id="ed5-vol1",
        ),
        param(
            Edition.FIVE,
            Volume.TWO,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1843",
            id="ed5-vol2",
        ),
        param(
            Edition.SIX,
            Volume.ONE,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1850",
            id="ed6-vol1",
        ),
        param(
            Edition.SIX,
            Volume.TWO,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1850",
            id="ed6-vol2",
        ),
        param(
            Edition.SEVEN,
            Volume.ONE,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1857",
            id="ed7-vol1",
        ),
        param(
            Edition.SEVEN,
            Volume.TWO,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1857",
            id="ed7-vol2",
        ),
    ),
)
def test_get_download_link(edition: Edition, volume: Volume, expected_link: str):
    link = get_download_link(edition, volume)
    assert link == expected_link


def test_get_source_document_as_raw_bytes():
    expected = b"<!doctype html>"
    actual = get_source_document_as_raw_bytes("http://example.com/")
    assert actual.startswith(expected)

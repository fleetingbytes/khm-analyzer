from pytest import mark, param
from khm_analyzer.download import publication_year, get_download_link, get_source_document_as_raw_bytes


@mark.parametrize(
    "edition, volume, expected_year",
    (
        param(1, 1, 1812, id="ed1-vol1"),
        param(1, 2, 1815, id="ed1-vol2"),
        param(2, 1, 1819, id="ed2-vol1"),
        param(2, 2, 1819, id="ed2-vol2"),
        param(3, 1, 1837, id="ed3-vol1"),
        param(3, 2, 1837, id="ed3-vol2"),
        param(4, 1, 1840, id="ed4-vol1"),
        param(4, 2, 1840, id="ed4-vol2"),
        param(5, 1, 1843, id="ed5-vol1"),
        param(5, 2, 1843, id="ed5-vol2"),
        param(6, 1, 1850, id="ed6-vol1"),
        param(6, 2, 1850, id="ed6-vol2"),
        param(7, 1, 1857, id="ed7-vol1"),
        param(7, 2, 1857, id="ed7-vol2"),
    ),
)
def test_publication_year(edition, volume, expected_year):
    year = publication_year(edition, volume)
    assert year == expected_year


@mark.parametrize(
    "edition, volume, expected_link",
    (
        param(
            1,
            1,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1812",
            id="ed1-vol1",
        ),
        param(
            1,
            2,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1815",
            id="ed1-vol2",
        ),
        param(
            2,
            1,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1819",
            id="ed2-vol1",
        ),
        param(
            2,
            2,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1819",
            id="ed2-vol2",
        ),
        param(
            3,
            1,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1837",
            id="ed3-vol1",
        ),
        param(
            3,
            2,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1837",
            id="ed3-vol2",
        ),
        param(
            4,
            1,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1840",
            id="ed4-vol1",
        ),
        param(
            4,
            2,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1840",
            id="ed4-vol2",
        ),
        param(
            5,
            1,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1843",
            id="ed5-vol1",
        ),
        param(
            5,
            2,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1843",
            id="ed5-vol2",
        ),
        param(
            6,
            1,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1850",
            id="ed6-vol1",
        ),
        param(
            6,
            2,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1850",
            id="ed6-vol2",
        ),
        param(
            7,
            1,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen01_1857",
            id="ed7-vol1",
        ),
        param(
            7,
            2,
            "https://deutschestextarchiv.de/book/download_lingxml/grimm_maerchen02_1857",
            id="ed7-vol2",
        ),
    ),
)
def test_get_download_link(edition, volume, expected_link):
    link = get_download_link(edition, volume)
    assert link == expected_link


def test_get_source_document_as_raw_bytes():
    expected = b"<!doctype html>"
    actual = get_source_document_as_raw_bytes("http://example.com/")
    assert actual.startswith(expected)

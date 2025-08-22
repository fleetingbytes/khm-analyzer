from pytest import mark, param
from lxml import etree 
from io import BytesIO

@mark.parametrize(
    "khm_edition_volume, expected_year",
    (
        param((1, 1), 1812, id="ed1-vol1"),
        param((1, 2), 1815, id="ed1-vol2"),
        param((2, 1), 1819, id="ed2-vol1"),
        param((2, 2), 1819, id="ed2-vol2"),
        param((3, 1), 1837, id="ed3-vol1"),
        param((3, 2), 1837, id="ed3-vol2"),
        param((4, 1), 1840, id="ed4-vol1"),
        param((4, 2), 1840, id="ed4-vol2"),
        param((5, 1), 1843, id="ed5-vol1"),
        param((5, 2), 1843, id="ed5-vol2"),
        param((6, 1), 1850, id="ed6-vol1"),
        param((6, 2), 1850, id="ed6-vol2"),
        param((7, 1), 1857, id="ed7-vol1"),
        param((7, 2), 1857, id="ed7-vol2"),
    ),
    indirect=("khm_edition_volume", ),
)
def test_publication_year(khm_edition_volume, expected_year):
    tree = etree.parse(BytesIO(khm_edition_volume))
    root = tree.getroot()
    xpath = etree.XPath("""//ns:publicationStmt/ns:date[@type="publication"]""", namespaces={"ns": root.nsmap[None]})
    filtered = filter(lambda date_tag: date_tag.text == str(expected_year), xpath(root))
    date_tag = next(filtered)
    assert date_tag is not None


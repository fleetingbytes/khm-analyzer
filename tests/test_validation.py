from pytest import mark, param, warns
from io import TextIOWrapper, BytesIO
from khm_analyzer.validation import correct_buffer, CorrectionData
from lxml import etree
from khm_analyzer.utils import set_stream_position_to_the_start
from khm_analyzer.warnings import InvalidXmlCorrectedWarning


@mark.parametrize(
    "khm_edition_volume",
    (param((3, 1), id="ed3-vol1"),),
    indirect=("khm_edition_volume",),
)
def test_correct_buffer(khm_edition_volume):
    raw_bytes = khm_edition_volume
    wrong_buffer = TextIOWrapper(BytesIO(raw_bytes), encoding="UTF-8")

    try:
        etree.parse(wrong_buffer)
    except etree.XMLSyntaxError as err:
        correction_data = CorrectionData(err)
        set_stream_position_to_the_start(wrong_buffer)

    with warns(InvalidXmlCorrectedWarning, match="Corrected"):
        corrected_buffer = correct_buffer(wrong_buffer, correction_data)

    lines = corrected_buffer.readlines()
    assert correction_data.corrected_substring in lines[correction_data.wrong_line_number - 1]

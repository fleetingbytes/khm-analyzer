from io import TextIOWrapper, BytesIO
from pathlib import Path
from human_regex import StringRegex
from lxml import etree
from .utils import set_stream_position_to_the_start, get_file_name_from_buffer
from .warnings import InvalidXmlCorrectedWarning
from warnings import warn
from logging import getLogger, disable as disable_logging, NOTSET

logger = getLogger(__name__)

CORRECTABLE_ERROR_CODE = 513
MAXIMUM_CORRECTIONS_PER_RUN = 3


class CorrectionData:
    def __init__(self, err: etree.XMLSyntaxError):
        self.err = err
        self._wrong_xmlid = None

    @property
    def error_message(self) -> str:
        return self.err.msg

    @property
    def correction_possible(self) -> bool:
        return self.err.code == CORRECTABLE_ERROR_CODE

    @property
    def wrong_line_number(self) -> int:
        return self.err.lineno

    @property
    def wrong_xmlid(self) -> str:
        if self._wrong_xmlid is None:
            xmlid_regex = StringRegex(r"\S").one_or_more.named("xmlid").preceded_by("ID ")
            match = xmlid_regex.search(self.err.msg)
            assert match, "Cannot find wrong xml:id in error message"
            xmlid = match.group("xmlid")
            self._wrong_xmlid = xmlid
        return self._wrong_xmlid

    @property
    def wrong_substring(self) -> str:
        return f'xml:id="{self.wrong_xmlid}"'

    @property
    def corrected_substring(self) -> str:
        return f'xml:id="corrected_{self.wrong_xmlid}"'


def validate_paths(paths: list[Path], correction_wanted: bool) -> None:
    logger.debug("Validating paths %s", paths)
    for path in paths:
        with path.open(mode="r", encoding="UTF-8") as file:
            logger.debug("Opened %s for reading", path.name)
            is_valid, correction_data = check_xml(file)
            if is_valid:
                print(path, "is valid XML")
                break
            else:
                print(correction_data.error_message)
        logger.debug("Closed %s", path.name)
        if correction_wanted and correction_data.correction_possible:
            correct_file_in_path(path, correction_data)

def validate_directories(directories: list[Path], correction_wanted: bool) -> None:
    for directory in directories:
        paths_in_directory = directory.glob("*")
        files_in_directory = filter(lambda file: file.is_file, paths_in_directory)
        validate_paths(sorted(files_in_directory), correction_wanted)

def correct_file_in_path(path: Path, correction_data: CorrectionData) -> None:
    with path.open(mode="r", encoding="UTF-8") as wrong_file:
        logger.debug("Opened %s for reading", path.name)
        wrong_buffer = wrong_file
        for _ in range(MAXIMUM_CORRECTIONS_PER_RUN):
            corrected_buffer = correct_buffer(wrong_buffer, correction_data)
            is_valid, correction_data = check_xml(corrected_buffer)
            if is_valid:
                break
            wrong_buffer = corrected_buffer
    logger.debug("Closed %s", path.name)
    with path.open("w", encoding="UTF-8") as corrected_file:
        logger.debug("Opened %s for writing", path.name)
        corrected_file.write(corrected_buffer.read())
        logger.debug("Wrote %s into %s", corrected_buffer, path.name)
    logger.debug("Closed %s", path.name)

def correct_buffer(buffer: TextIOWrapper, correction_data: CorrectionData) -> TextIOWrapper:
    corrected_buffer = BytesIO()
    corrected_wrapper = TextIOWrapper(corrected_buffer, encoding="UTF-8")
    logger.debug("Created corrected wrapper %r", corrected_wrapper)

    for line_number, line in enumerate(buffer, start=1):
        if line_number != correction_data.wrong_line_number:
            corrected_wrapper.write(line)
        else:
            wrong_substring = correction_data.wrong_substring
            corrected_substring = correction_data.corrected_substring

            corrected_line = line.replace(wrong_substring, corrected_substring)
            corrected_wrapper.write(corrected_line)
            warn(
                InvalidXmlCorrectedWarning(
                    wrong_substring,
                    corrected_substring,
                    line_number
                ),
                stacklevel=1,
            )
            logger.debug("Wrote corrected line %d into the wrapper %r", line_number, corrected_wrapper)

    set_stream_position_to_the_start(corrected_wrapper)
    return corrected_wrapper

def check_xml(buffer: TextIOWrapper | BytesIO) -> tuple[bool, CorrectionData | None]:
    try:
        _ = etree.parse(buffer)
        validity = "valid"
        correction_data = None
    except etree.XMLSyntaxError as err:
        validity = "not valid"
        correction_data = CorrectionData(err)

    file_name = get_file_name_from_buffer(buffer)
    logger.debug("Buffer for %s is %s", file_name, validity)
    set_stream_position_to_the_start(buffer)

    return not correction_data, correction_data

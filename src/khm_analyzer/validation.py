from io import TextIOWrapper, BytesIO
from pathlib import Path
from lxml import etree
from .utils import set_stream_position_to_the_start, get_file_name_from_buffer, debug
from .warnings import InvalidXmlCorrectedWarning, FileNotCorrectedWarning
from warnings import warn
from logging import getLogger

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
            xmlid_regex = r"(?<=ID )(?P<xmlid>\S+)"
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


def validate_directories(directories: list[Path], correction_wanted: bool) -> None:
    for directory in directories:
        paths_in_directory = directory.glob("*")
        files_in_directory = filter(lambda file: file.is_file, paths_in_directory)
        validate_paths(sorted(files_in_directory), correction_wanted)


@debug
def validate_paths(paths: list[Path], correction_wanted: bool) -> None:
    for path in paths:
        with path.open(mode="r", encoding="UTF-8") as file:
            is_valid, correction_data = check_xml(file)
            if is_valid:
                print(path, "is valid XML")
            else:
                print(path, "is invalid XML", correction_data.error_message)
        if (not is_valid) and correction_wanted and correction_data.correction_possible:
            correct_file_in_path(path, correction_data)


def correct_file_in_path(path: Path, correction_data: CorrectionData) -> None:
    corrected_buffer = try_to_correct_buffer(path, correction_data)
    write_buffer_to_path(corrected_buffer, path)


@debug
def try_to_correct_buffer(path: Path, correction_data: CorrectionData) -> TextIOWrapper:
    with path.open(mode="r", encoding="UTF-8") as wrong_file:
        wrong_buffer = wrong_file
        for _ in range(MAXIMUM_CORRECTIONS_PER_RUN):
            corrected_buffer = correct_buffer(wrong_buffer, correction_data)
            is_valid, correction_data = check_xml(corrected_buffer)
            if is_valid:
                break
            wrong_buffer = corrected_buffer
    if not is_valid:
        warn(FileNotCorrectedWarning(path))
    return corrected_buffer


@debug
def write_buffer_to_path(buffer: TextIOWrapper, path: Path) -> None:
    with path.open("w", encoding="UTF-8") as corrected_file:
        corrected_file.write(buffer.read())


def correct_buffer(buffer: TextIOWrapper, correction_data: CorrectionData) -> TextIOWrapper:
    corrected_buffer = BytesIO()
    corrected_wrapper = TextIOWrapper(corrected_buffer, encoding="UTF-8")

    for line_number, line in enumerate(buffer, start=1):
        if line_number == correction_data.wrong_line_number:
            line = correct_line(line, correction_data)
            logger.info("Writing corrected line %d into the wrapper %r", line_number, corrected_wrapper)
        corrected_wrapper.write(line)

    set_stream_position_to_the_start(corrected_wrapper)
    return corrected_wrapper


def correct_line(line: str, data: CorrectionData) -> str:
    corrected_line = line.replace(data.wrong_substring, data.corrected_substring)
    warn(
        InvalidXmlCorrectedWarning(data.wrong_substring, data.corrected_substring, data.wrong_line_number),
        stacklevel=1,
    )
    return corrected_line


def check_xml(buffer: TextIOWrapper | BytesIO) -> tuple[bool, CorrectionData | None]:
    try:
        _ = etree.parse(buffer)
        correction_data = None
    except etree.XMLSyntaxError as err:
        correction_data = CorrectionData(err)

    buffer_is_valid = calculate_and_log_buffer_validity(buffer, correction_data)
    set_stream_position_to_the_start(buffer)

    return buffer_is_valid, correction_data


def calculate_and_log_buffer_validity(buffer: TextIOWrapper, data: CorrectionData) -> bool:
    buffer_is_valid = not bool(data)
    validity = "valid" if buffer_is_valid else "not valid"

    file_name = get_file_name_from_buffer(buffer)
    logger.debug("Buffer %s is %s", file_name, validity)

    return buffer_is_valid

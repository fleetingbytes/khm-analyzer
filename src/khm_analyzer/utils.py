from io import IOBase, TextIOWrapper, BytesIO
from os import SEEK_SET
from pathlib import Path
from logging import getLogger


logger = getLogger(__name__)

def set_stream_position_to_the_start(buffer: IOBase) -> None:
    logger.debug("Position reset to start in %s", get_file_name_from_buffer(buffer))
    _ = buffer.seek(0, SEEK_SET)


def get_file_name_from_buffer(buffer: TextIOWrapper) -> str:
    try:
        return Path(buffer.name).name
    except AttributeError:
        return f"{buffer} Id: {id(buffer)}"

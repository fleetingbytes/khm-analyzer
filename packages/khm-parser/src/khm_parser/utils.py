from __future__ import annotations

from logging import getLogger
from os import SEEK_END, SEEK_SET
from pathlib import Path
from typing import TYPE_CHECKING

from khm_parser.constants import ELEMENTS_MAP

if TYPE_CHECKING:
    from io import IOBase, TextIOWrapper

    from .bases import KHMElement

logger = getLogger(__name__)


def get_class_with_dtaid(tag_name: str, dtaid: int, default: None = None) -> KHMElement | None:
    cls = ELEMENTS_MAP.get(tag_name, default)
    if cls is not default:
        cls.DTAID = dtaid
    return cls


def set_stream_position_to_the_start(buffer: IOBase) -> int:
    new_position = buffer.seek(0, SEEK_SET)
    logger.debug("Position reset to start of %s", get_file_name_from_buffer(buffer))
    return new_position


def set_stream_position_to_the_end(buffer: IOBase) -> int:
    new_position = buffer.seek(0, SEEK_END)
    logger.debug("Position reset to the end of %s", get_file_name_from_buffer(buffer))
    return new_position


def set_stream_position(position: int, buffer: IOBase) -> int:
    new_position = buffer.seek(position, SEEK_SET)
    logger.debug("Position reset to %d in %s", position, get_file_name_from_buffer(buffer))
    return new_position


def shorten_stream_by(num: int, buffer: IOBase) -> None:
    position = set_stream_position_to_the_end(buffer)
    logger.debug("Truncating stream %s at position %d", get_file_name_from_buffer(buffer), num)
    new_buffer_end_position = buffer.truncate(position - num)
    set_stream_position(new_buffer_end_position, buffer)


def get_file_name_from_buffer(buffer: TextIOWrapper) -> str:
    try:
        return Path(buffer.name).name
    except AttributeError:
        return f"{buffer} Id: {id(buffer)}"

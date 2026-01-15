from __future__ import annotations

from logging import getLogger
from os import SEEK_SET
from pathlib import Path
from typing import TYPE_CHECKING

from khm_analyzer.constants import ELEMENTS_MAP

if TYPE_CHECKING:
    from io import IOBase, TextIOWrapper

    from .bases import KHMElement

logger = getLogger(__name__)


def get_class_with_dtaid(tag_name: str, dtaid: int, default: None = None) -> KHMElement | None:
    cls = ELEMENTS_MAP.get(tag_name, default)
    if cls is not default:
        cls.DTAID = dtaid
    return cls


def set_stream_position_to_the_start(buffer: IOBase) -> None:
    logger.debug("Position reset to start in %s", get_file_name_from_buffer(buffer))
    _ = buffer.seek(0, SEEK_SET)


def get_file_name_from_buffer(buffer: TextIOWrapper) -> str:
    try:
        return Path(buffer.name).name
    except AttributeError:
        return f"{buffer} Id: {id(buffer)}"

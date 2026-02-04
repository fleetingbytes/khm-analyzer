from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from io import StringIO
from logging import getLogger

from khm_parser.utils import shorten_stream_by

from .dtaids import KHM_ED1_VOL1

logger = getLogger(__name__)


@dataclass(frozen=True, eq=True)
class CorrectionId:
    dtaid: int
    xmlid: str


def add_space_at_the_end(buffer: StringIO) -> StringIO:
    buffer.write(" ")
    return buffer


def remove_final_char(buffer: StringIO) -> StringIO:
    logger.debug("Correction: Remove one character at the end of the buffer")
    shorten_stream_by(1, buffer)
    return buffer


Corrections = dict[CorrectionId, Callable[[StringIO], StringIO]]

default_corrections = {
    CorrectionId(KHM_ED1_VOL1, "s112"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s112_2"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s939"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s939_2"): add_space_at_the_end,
}

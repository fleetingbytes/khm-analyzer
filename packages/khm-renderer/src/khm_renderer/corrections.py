from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from io import StringIO
from logging import getLogger

from .dtaids import KHM_ED1_VOL1

logger = getLogger(__name__)


@dataclass(frozen=True, eq=True)
class CorrectionId:
    dtaid: int
    xmlid: str


def add_space_at_the_end(buffer: StringIO) -> StringIO:
    buffer.write(" ")
    return buffer


def remove_space_at_the_end(buffer: StringIO) -> StringIO:
    logger.debug("Correction: Remove space at the end of the buffer")
    position = buffer.tell()
    buffer.truncate(position - 1)
    return buffer


Corrections = dict[CorrectionId, Callable[[StringIO], StringIO]]

default_corrections = {
    CorrectionId(KHM_ED1_VOL1, "s112"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s112_2"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s939"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s939_2"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "sffb_2"): remove_space_at_the_end,
}

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from io import StringIO

from .dtaids import KHM_ED1_VOL1


@dataclass(frozen=True, eq=True)
class CorrectionId:
    dtaid: int
    xmlid: str


def add_space_at_the_end(buffer: StringIO):
    buffer.write(" ")
    return buffer


Corrections = dict[CorrectionId, Callable[[StringIO], StringIO]]

corrections = {
    CorrectionId(KHM_ED1_VOL1, "s112"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s112_2"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s939"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s939_2"): add_space_at_the_end,
}

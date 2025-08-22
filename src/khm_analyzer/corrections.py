from dataclasses import dataclass
from .dtaids import KHM_ED1_VOL1
from io import StringIO


@dataclass(frozen=True, eq=True)
class CorrectionId:
    dtaid: int
    xmlid: str

def add_space_at_the_end(buffer: StringIO):
    buffer.write(" ")
    return buffer

corrections = {
    CorrectionId(KHM_ED1_VOL1, "s112"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s112_2"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s939"): add_space_at_the_end,
    CorrectionId(KHM_ED1_VOL1, "s939_2"): add_space_at_the_end,
}

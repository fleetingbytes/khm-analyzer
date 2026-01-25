from enum import IntEnum, auto, unique


@unique
class Volume(IntEnum):
    ONE = auto()
    TWO = auto()


@unique
class Edition(IntEnum):
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()


class ReturnCode(IntEnum):
    OK = 0
    ERROR = 1
    INVALID_XML = 2

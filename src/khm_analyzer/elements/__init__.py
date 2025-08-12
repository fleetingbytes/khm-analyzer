from ..bases import KHMElement
from .tale import Tale
from .title import Title
from .paragraph import Paragraph
from .linegroup import LineGroup
from .line import Line
from .sentence import Sentence
from .word import Word


ELEMENTS_MAP = {
    "div": Tale,
    "head": Title,
    "p": Paragraph,
    "lg": LineGroup,
    "l": Line,
    "s": Sentence,
    "w": Word,
}

def get_class_with_dtaid(tag_name: str, dtaid: int, default: None = None) -> KHMElement | None:
    cls = ELEMENTS_MAP.get(tag_name, default)
    if cls is not default:
        cls.DTAID = dtaid
    return cls

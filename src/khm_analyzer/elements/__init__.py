from ..bases import KHMElement
from .tale import Tale
from .title import Title
from .paragraph import Paragraph
from .linegroup import LineGroup
from .line import Line
from .sentence_part import SentencePart
from .word_part import WordPart


ELEMENTS_MAP = {
    "div": Tale,
    "head": Title,
    "p": Paragraph,
    "lg": LineGroup,
    "l": Line,
    "s": SentencePart,
    "w": WordPart,
}

def get_class_with_dtaid(tag_name: str, dtaid: int, default: None = None) -> KHMElement | None:
    cls = ELEMENTS_MAP.get(tag_name, default)
    if cls is not default:
        cls.DTAID = dtaid
    return cls

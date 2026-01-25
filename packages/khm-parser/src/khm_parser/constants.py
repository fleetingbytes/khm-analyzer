from .elements.line import Line
from .elements.linegroup import LineGroup
from .elements.paragraph import Paragraph
from .elements.sentence_part import SentencePart
from .elements.tale import Tale
from .elements.title import Title
from .elements.word_part import WordPart

ELEMENTS_MAP = {
    "div": Tale,
    "head": Title,
    "p": Paragraph,
    "lg": LineGroup,
    "l": Line,
    "s": SentencePart,
    "w": WordPart,
}

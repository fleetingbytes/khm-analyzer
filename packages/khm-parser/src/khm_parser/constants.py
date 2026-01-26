from khm_parser.elements.head import Head
from khm_parser.elements.line import Line
from khm_parser.elements.linegroup import LineGroup
from khm_parser.elements.paragraph import Paragraph
from khm_parser.elements.sentence_part import SentencePart
from khm_parser.elements.tale import Tale
from khm_parser.elements.word_part import WordPart

ELEMENTS_MAP = {
    "div": Tale,
    "head": Head,
    "p": Paragraph,
    "lg": LineGroup,
    "l": Line,
    "s": SentencePart,
    "w": WordPart,
}

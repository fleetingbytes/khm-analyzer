from .tale import Tale
from .title import Title
from .paragraph import Paragraph
from .sentence import Sentence
from .word import Word


ELEMENTS_MAP = {
    "div": Tale,
    "head": Title,
    "p": Paragraph,
    "s": Sentence,
    "w": Word,
}

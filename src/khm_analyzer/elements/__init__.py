from .tale import Tale
from .head import Head
from .paragraph import Paragraph
from .sentence import Sentence
from .word import Word


ELEMENTS_MAP = {
    "div": Tale,
    "head": Head,
    "p": Paragraph,
    "s": Sentence,
    "w": Word,
}

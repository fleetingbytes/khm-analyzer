from dataclasses import dataclass

DEFAULT_WORD_PART_SEPARATOR = ""
DEFAULT_WORD_SEPARATOR = " "
DEFAULT_SENTENCE_PART_SEPARATOR = " "
DEFAULT_SENTENCE_SEPARATOR = " "
DEFAULT_PARAGRAPH_SEPARATOR = "\n\n"


@dataclass(slots=True)
class Separators:
    word_part: str = DEFAULT_WORD_PART_SEPARATOR
    word: str = DEFAULT_WORD_SEPARATOR
    sentence_part: str = DEFAULT_SENTENCE_PART_SEPARATOR
    sentence: str = DEFAULT_SENTENCE_SEPARATOR
    paragraph: str = DEFAULT_PARAGRAPH_SEPARATOR

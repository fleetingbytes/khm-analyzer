from ..bases import WordBase
from lxml import etree
from enum import Flag, auto


class Join(Flag):
    NONE = 0
    LEFT = auto()
    RIGHT = auto()
    BOTH = LEFT | RIGHT


JOIN_MAP = {
    "left": Join.LEFT,
    "right": Join.RIGHT,
    "both": Join.BOTH,
    None: Join.NONE,
}
class Word(WordBase):
    @property
    def join(self) -> Join:
        value = self.get("join")
        result = JOIN_MAP[value]
        return result

    @property
    def needs_space_left(self) -> bool:
        return not self.join & Join.LEFT

    @property
    def needs_space_right(self) -> bool:
        return not self.join & Join.RIGHT

    def remove_redundant_space_left(self, word: str) -> str:
        if not self.needs_space_left:
            return word.lstrip()
        return word

    def remove_redundant_space_right(self, word: str) -> str:
        if not self.needs_space_right:
            return word.rstrip()
        return word

    def remove_redundant_spaces(self, word: str) -> str:
        word = self.remove_redundant_space_left(word)
        word = self.remove_redundant_space_right(word)
        return word

    def render(self) -> str:
        norm = self.get("norm", default="")
        word_with_potentially_redundant_spaces = f" {norm} "
        word = self.remove_redundant_spaces(word_with_potentially_redundant_spaces)
        return word


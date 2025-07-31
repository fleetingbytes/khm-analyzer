from collections.abc import Iterable
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
    def joins_word_left(self) -> bool:
        return self.join & Join.LEFT

    @property
    def joins_word_right(self) -> bool:
        return self.join & Join.RIGHT

    @property
    def normalized_transcription(self) -> str:
        normalized = self.get("norm", default="")
        return normalized

    @staticmethod
    def contract_final_es(transcribed_word: str) -> str:
        if transcribed_word.endswith("_es"):
            return transcribed_word.replace("_e", "")
        return transcribed_word

    def render(self) -> str:
        norm = self.normalized_transcription
        contracted = self.contract_final_es(norm)
        return contracted

    @property
    def following_words(self) -> Iterable[WordBase]:
        return self.itersiblings(tag=WordBase.TAG, preceding=False)

    @property
    def is_last_in_sentence(self) -> bool:
        try:
            _ = next(self.following_words)
            return False
        except StopIteration:
            return True

    @property
    def is_nth_part(self) -> bool:
        previous_word_id = self.get("prev", None)
        return bool(previous_word_id)

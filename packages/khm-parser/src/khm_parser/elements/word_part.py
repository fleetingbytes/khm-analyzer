from collections.abc import Iterable
from enum import Flag, auto

from ..bases import WordPartBase
from ..namespace import tei_namespace


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


class WordPart(WordPartBase):
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
        contracted = self.contract_final_es(normalized)
        return contracted

    @staticmethod
    def contract_final_es(transcribed_word: str) -> str:
        if transcribed_word.endswith("_es"):
            return transcribed_word.replace("_e", "")
        return transcribed_word

    @property
    def is_the_final_part(self) -> bool:
        return not self.joins_word_right and not self.has_a_following_part

    @property
    def following_words(self) -> Iterable[WordPartBase]:
        return self.itersiblings(tag=WordPartBase.TAG, preceding=False)

    @property
    def is_last_in_sentencepart(self) -> bool:
        try:
            _ = next(self.following_words)
            return False
        except StopIteration:
            return True

    @property
    def is_nth_part(self) -> bool:
        previous_word_id = self.get("prev", None)
        return bool(previous_word_id)

    @property
    def has_a_following_part(self) -> bool:
        following_part = self.get("next", None)
        return bool(following_part)

    @property
    def is_a_part_before_page_break(self) -> bool:
        if self.has_a_following_part:
            try:
                following_element = next(self.itersiblings())
                following_element_is_a_page_break = following_element.tag == tei_namespace("pb")
                return following_element_is_a_page_break
            except StopIteration:
                return False
        return False

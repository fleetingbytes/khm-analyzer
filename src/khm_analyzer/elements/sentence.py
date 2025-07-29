from ..bases import SentenceBase, WordBase
from collections.abc import Iterable


class Sentence(SentenceBase):
    @property
    def words(self) -> Iterable[WordBase]:
        yield from self.iterdescendants(tag=WordBase.TAG)

    @staticmethod
    def sanitize_spaces(text: str) -> str:
        return text.replace("  ", " ")

    def render(self) -> str:
        sentence_with_double_spaces = "".join(word.render() for word in self.words)
        sentence = self.sanitize_spaces(sentence_with_double_spaces)
        return sentence.strip()

from ..bases import HeadBase, SentenceBase
from lxml import etree
from collections.abc import Iterable


class Head(HeadBase):
    @property
    def _sentences(self) -> Iterable[SentenceBase]:
        yield from self.iterdescendants(tag=SentenceBase.TAG)

    @property
    def number(self) -> int | None:
        first_sentence = next(self._sentences).render()
        number_without_trailing_full_stop = first_sentence.rstrip(".")
        try:
            tale_number = int(number_without_trailing_full_stop)
            return tale_number
        except TypeError:
            return None

    @property
    def _first_sentence_is_a_number(self) -> bool:
        return self.number is not None

    def render(self) -> str:
        meaningful_sentences = list(self._sentences)
        if self._first_sentence_is_a_number:
            meaningful_sentences = meaningful_sentences[1:]
        head = "\n".join(sentence.render() for sentence in meaningful_sentences)
        return head

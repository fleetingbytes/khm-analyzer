from ..bases import HeadBase, SentenceBase
from lxml import etree
from collections.abc import Iterable


class Head(HeadBase):
    @property
    def sentences(self) -> Iterable[SentenceBase]:
        yield from self.iterdescendants(tag=SentenceBase.TAG)

    @property
    def number(self) -> int | None:
        first_sentence = next(self.sentences).render()
        first_sentence_without_trailing_full_stop = first_sentence.rstrip(".")
        try:
            tale_number = int(first_sentence_without_trailing_full_stop)
            return tale_number
        except TypeError:
            return None

    @property
    def first_sentence_is_a_number(self) -> bool:
        return self.number is not None

    def render(self) -> str:
        meaningful_sentences = list(self.sentences)
        if self.first_sentence_is_a_number:
            meaningful_sentences = meaningful_sentences[1:]
        head = "\n".join(sentence.render() for sentence in meaningful_sentences)
        return head

    @property
    def head_text(self) -> str:
        text = etree.tostring(self, method="text", encoding="unicode")
        return text


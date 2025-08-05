from ..bases import ParagraphBase, SentenceBase
from collections.abc import Iterable


class Paragraph(ParagraphBase):
    @property
    def sentences(self) -> Iterable[SentenceBase]:
        yield from self.iterdescendants(tag=SentenceBase.TAG)

    def render(self, sentence_separator: str) -> str:
        paragraph = sentence_separator.join(sentence.render() for sentence in self.sentences)
        return paragraph

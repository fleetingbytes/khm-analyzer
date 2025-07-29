from ..bases import ParagraphBase, SentenceBase
from collections.abc import Iterable


class Paragraph(ParagraphBase):
    @property
    def sentences(self) -> Iterable[SentenceBase]:
        yield from self.iterdescendants(tag=SentenceBase.TAG)

    def render(self) -> str:
        paragraph = " ".join(sentence.render() for sentence in self.sentences)
        return paragraph

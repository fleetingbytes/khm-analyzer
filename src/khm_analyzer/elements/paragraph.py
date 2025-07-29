from ..bases import ParagraphBase, SentenceBase


class Paragraph(ParagraphBase):
    def render(self) -> str:
        paragraph = "\n".join(sentence.render() for sentence in self.iterdescendants(tag=SentenceBase.TAG))
        return paragraph

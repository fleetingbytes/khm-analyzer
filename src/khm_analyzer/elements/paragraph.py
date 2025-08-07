from ..bases import ParagraphBase, SentenceBase
from collections.abc import Iterable
from io import StringIO


class Paragraph(ParagraphBase):
    @property
    def sentences(self) -> Iterable[SentenceBase]:
        yield from self.iterdescendants(tag=SentenceBase.TAG)

    def render(self, sentence_separator: str) -> str:
        buffer = StringIO()

        for sentence in self.sentences:
            buffer.write(sentence.render())

            # Certain sentences are split into multiple parts, e.g. "s11a" in khm-ed1-vol1.
            # Such sentences have a `next` attribute which contains the xml:id of the following sentence.
            # We don't want to type a space after such sentence parts.
            if sentence.has_a_following_part:
                continue
            buffer.write(sentence_separator)

        paragraph_with_trailing_white_space = buffer.getvalue()
        paragraph_without_trailing_white_space = paragraph_with_trailing_white_space.rstrip(sentence_separator)

        return paragraph_without_trailing_white_space

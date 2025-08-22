from collections.abc import Iterable
from ..bases import TaleBase, TitleBase, ParagraphBase
from io import StringIO


class Tale(TaleBase):
    @property
    def title(self) -> TitleBase:
        return next(self.iter(tag=TitleBase.TAG))

    @property
    def paragraphs(self) -> Iterable[str]:
        yield from self.iter(tag=ParagraphBase.TAG)

    def render(self, number: bool=False, title: bool=False, one_sentence_per_line: bool=False, **kwargs) -> str:
        buffer = StringIO()

        if metadata := self.metadata(number=number, title=title):
            buffer.write(metadata)
            buffer.write("\n\n")

        sentence_separator = "\n" if one_sentence_per_line else " "
        rendered_paragraphs = "\n\n".join(paragraph.render(sentence_separator=sentence_separator, **kwargs) for paragraph in self.paragraphs)
        buffer.write(rendered_paragraphs)

        return buffer.getvalue()

    def render_title(self) -> str:
        return self.title.render()

    @property
    def number(self) -> int:
        return self.title.number

    def metadata(self, number: bool, title: bool) -> str:
        buffer = StringIO()

        if number:
            buffer.write(f"{self.number}. ")
        if title:
            buffer.write(self.render_title())

        return buffer.getvalue().rstrip()

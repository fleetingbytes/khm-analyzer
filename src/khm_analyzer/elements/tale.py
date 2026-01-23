from collections.abc import Iterable
from io import StringIO

from ..bases import ParagraphBase, TaleBase, TitleBase
from ..separators import (
    DEFAULT_PARAGRAPH_SEPARATOR,
    DEFAULT_SENTENCE_PART_SEPARATOR,
    DEFAULT_SENTENCE_SEPARATOR,
    DEFAULT_WORD_PART_SEPARATOR,
    DEFAULT_WORD_SEPARATOR,
)


class Tale(TaleBase):
    @property
    def head(self) -> TitleBase:
        return next(self.iter(tag=TitleBase.TAG))

    @property
    def paragraphs(self) -> Iterable[str]:
        yield from self.iter(tag=ParagraphBase.TAG)

    def render(
        self,
        *,
        show_number: bool = False,
        show_title: bool = False,
        sentence_separator: str | None = None,
        sentence_part_separator: str | None = None,
        word_separator: str | None = None,
        word_part_separator: str | None = None,
        paragraph_separator: str | None = None,
    ) -> str:
        sentence_separator = (
            sentence_separator if sentence_separator is not None else DEFAULT_SENTENCE_SEPARATOR
        )
        sentence_part_separator = (
            sentence_part_separator
            if sentence_part_separator is not None
            else DEFAULT_SENTENCE_PART_SEPARATOR
        )
        word_separator = word_separator if word_separator is not None else DEFAULT_WORD_SEPARATOR
        word_part_separator = (
            word_part_separator if word_part_separator is not None else DEFAULT_WORD_PART_SEPARATOR
        )
        paragraph_separator = (
            paragraph_separator if paragraph_separator is not None else DEFAULT_PARAGRAPH_SEPARATOR
        )

        buffer = StringIO()

        if metadata := self.metadata(
            show_number=show_number,
            show_title=show_title,
            sentence_part_separator=sentence_part_separator,
            word_separator=word_separator,
            word_part_separator=word_part_separator,
        ):
            buffer.write(metadata)
            buffer.write(paragraph_separator)

        rendered_paragraphs = paragraph_separator.join(
            paragraph.render(
                sentence_separator=sentence_separator,
                sentence_part_separator=sentence_part_separator,
                word_separator=word_separator,
                word_part_separator=word_part_separator,
            )
            for paragraph in self.paragraphs
        )
        buffer.write(rendered_paragraphs)

        return buffer.getvalue()

    def title(
        self,
        sentence_part_separator: str | None = None,
        word_separator: str | None = None,
        word_part_separator: str | None = None,
    ) -> str:
        return self.head.render(
            sentence_part_separator=sentence_part_separator,
            word_separator=word_separator,
            word_part_separator=word_part_separator,
        )

    @property
    def number(self) -> int | None:
        return self.head.number

    def metadata(
        self,
        show_number: bool,
        show_title: bool,
        sentence_part_separator: str | None = None,
        word_separator: str | None = None,
        word_part_separator: str | None = None,
    ) -> str:
        buffer = StringIO()

        if show_number:
            buffer.write(f"{self.number}.{sentence_part_separator}")
        if show_title:
            buffer.write(
                self.title(
                    sentence_part_separator=sentence_part_separator,
                    word_separator=word_separator,
                    word_part_separator=word_part_separator,
                )
            )

        return buffer.getvalue().rstrip()

from collections.abc import Iterable
from io import StringIO

from khm_parser.bases import HeadBase, ParagraphBase, TaleBase


class Tale(TaleBase):
    @property
    def head(self) -> HeadBase:
        return next(self.iter(tag=HeadBase.TAG))

    @property
    def paragraphs(self) -> Iterable[str]:
        yield from self.iter(tag=ParagraphBase.TAG)

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

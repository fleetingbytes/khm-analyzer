from __future__ import annotations

from typing import TYPE_CHECKING

from khm_parser.bases import HeadBase, ParagraphBase, TaleBase

if TYPE_CHECKING:
    from collections.abc import Generator

    from khm_parser.elements import Head, Paragraph


class Tale(TaleBase):
    @property
    def head(self) -> Head:
        return next(self.iter(tag=HeadBase.TAG))

    @property
    def paragraphs(self) -> Generator[Paragraph]:
        yield from self.iter(tag=ParagraphBase.TAG)

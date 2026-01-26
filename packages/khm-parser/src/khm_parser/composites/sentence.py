from __future__ import annotations

from typing import TYPE_CHECKING

from khm_parser.bases import SentenceBase

if TYPE_CHECKING:
    from collections.abc import Generator


class Sentence(SentenceBase):
    @property
    def words(self) -> Generator[str]:
        for sentence_part in self.parts:
            yield from sentence_part.words

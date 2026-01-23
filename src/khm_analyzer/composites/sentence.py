from __future__ import annotations

from typing import TYPE_CHECKING

from ..bases import SentenceBase
from ..separators import DEFAULT_SENTENCE_PART_SEPARATOR

if TYPE_CHECKING:
    from collections.abc import Generator


class Sentence(SentenceBase):
    def render(self, *, sentence_part_separator: str | None = None, **kwargs) -> str:
        if sentence_part_separator is None:
            sentence_part_separator: str = DEFAULT_SENTENCE_PART_SEPARATOR
        return sentence_part_separator.join(part.render(**kwargs) for part in self.parts)

    @property
    def words(self) -> Generator[str]:
        for sentence_part in self.parts:
            yield from sentence_part.words

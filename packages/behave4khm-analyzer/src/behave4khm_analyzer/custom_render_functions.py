from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from khm_parser.elements import WordPart


def get_first_letter_of_word_part(word_part: WordPart) -> str:
    return next(iter(word_part.normalized_transcription), "")

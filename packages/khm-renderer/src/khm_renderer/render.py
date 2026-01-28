from __future__ import annotations

from typing import TYPE_CHECKING

from khm_renderer.separators import Separators

if TYPE_CHECKING:
    from collections.abc import Generator

    from khm_parser.composites import Sentence
    from khm_parser.elements import Head, WordPart
    from khm_renderer.corrections import Corrections


def render_tale_head(
    head: Head, sep: Separators | None = None, corrections: Corrections | None = None
) -> str:
    if sep is None:
        sep = Separators()
    return sep.sentence.join((render_tale_number(head.number), render_tale_title(head.title)))


def render_tale_number(word_part: WordPart) -> str:
    transcription: str = word_part.normalized_transcription
    number: str = transcription.removesuffix(".")
    return number


def render_tale_title(title: Generator[Sentence], *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()
    return sep.sentence.join(render_sentence(sentence) for sentence in title)


def render_sentence(sentence: Sentence, *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()
    return ""

from __future__ import annotations

from typing import TYPE_CHECKING

from khm_renderer.separators import Separators

if TYPE_CHECKING:
    from collections.abc import Generator

    from khm_parser.composites import Sentence, Word
    from khm_parser.elements import Head, SentencePart, WordPart
    from khm_renderer.corrections import Corrections


def render_tale_head(
    head: Head, sep: Separators | None = None, _corrections: Corrections | None = None
) -> str:
    if sep is None:
        sep = Separators()
    return sep.sentence.join((render_tale_number(head.number), render_tale_title(head.title)))


def render_tale_number(word_part: WordPart) -> str:
    transcription: str = render_word_part(word_part)
    number: str = transcription.removesuffix(".")
    return number


def render_tale_title(title: Generator[Sentence], *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()
    return sep.sentence.join(render_sentence(sentence) for sentence in title)


def render_sentence(sentence: Sentence, *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()
    return sep.sentence_part.join(render_sentence_part(sentence_part) for sentence_part in sentence)


def render_sentence_part(sentence_part: SentencePart, *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()
    return sep.word.join(render_word(word) for word in sentence_part)


def render_word(word: Word, *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()
    return sep.word_part.join(render_word_part(word_part) for word_part in word)


def render_word_part(word_part: WordPart, *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()
    return word_part.normalized_transcription

from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from readylog.decorators import info

from khm_parser.utils import shorten_stream_by
from khm_renderer.corrections import CorrectionId, default_corrections
from khm_renderer.separators import Separators

if TYPE_CHECKING:
    from collections.abc import Generator
    from io import StringIO

    from khm_parser.composites import Sentence, Word
    from khm_parser.elements import Head, SentencePart, WordPart
    from khm_renderer.corrections import Corrections

logger = getLogger(__name__)


def render_tale_head(
    head: Head,
    buffer: StringIO,
    *,
    sep: Separators | None = None,
    corrections: Corrections | None = None,
) -> StringIO:
    if sep is None:
        sep = Separators()
    if corrections is None:
        corr = default_corrections

    number: str = render_tale_number(head.number)
    buffer.write(number)
    buffer.write(".")
    buffer.write(sep.sentence)
    buffer = render_tale_title(head.title, buffer, sep=sep, corrections=corr)

    return buffer


def render_tale_number(word_part: WordPart) -> str:
    transcription: str = render_word_part(word_part)
    number: str = transcription.removesuffix(".")
    return number


@info
def render_tale_title(
    title: Generator[Sentence],
    buffer: StringIO,
    *,
    sep: Separators | None = None,
    corrections: Corrections | None = None,
) -> StringIO:
    if sep is None:
        sep = Separators()
    if corrections is None:
        corrections = default_corrections

    for num, sentence in enumerate(title, start=1):
        logger.debug("Rendering tale title Sentence %d, id: %s", num, sentence.id)
        buffer = render_sentence(sentence, buffer, sep=sep, corrections=corrections)

    logger.debug("Removing '.' at the end of the title")
    shorten_stream_by(1, buffer)

    return buffer


def render_sentence(
    sentence: Sentence,
    buffer: StringIO,
    *,
    sep: Separators | None = None,
    corrections: Corrections | None = None,
) -> StringIO:
    if sep is None:
        sep = Separators()
    if corrections is None:
        corrections = default_corrections

    for num, sentence_part in enumerate(sentence, start=1):
        logger.debug("Rendering SentencePart %d, id: %s", num, sentence_part.xmlid)
        buffer = render_sentence_part(sentence_part, buffer, sep=sep)

        if should_write_sentence_part_separator(sentence_part, sentence):
            logger.debug("Writing sentence part separator")
            buffer.write(sep.sentence_part)

        if correction := corrections.get(CorrectionId(sentence_part.DTAID, sentence_part.xmlid), False):
            logger.debug(
                "Found correction for SentencePart %s in dtaid %s",
                sentence_part.xmlid,
                sentence_part.DTAID,
            )
            buffer = correction(buffer)

    return buffer


def should_write_sentence_part_separator(sentence_part: SentencePart, sentence: Sentence) -> bool:
    this_is_the_last_sentence_part = sentence_part.xmlid == sentence.last_part.xmlid
    result = not this_is_the_last_sentence_part

    return result


def render_sentence_part(
    sentence_part: SentencePart, buffer: StringIO, *, sep: Separators | None = None
) -> StringIO:
    if sep is None:
        sep = Separators()

    for num, word in enumerate(sentence_part, start=1):
        logger.debug("Rendering Word %d, id: %s", num, word.id)
        buffer = render_word(word, buffer, sep=sep)

        if should_write_word_separator(word, sentence_part):
            logger.debug("Writing word separator")
            buffer.write(sep.word)

    return buffer


def should_write_word_separator(word: Word, sentence_part: SentencePart) -> bool:
    this_is_the_last_word_in_sentence_part = word.id == sentence_part.last_word.id
    joins_word_right = word.last_part.joins_word_right
    has_a_normalized_transcription = word.last_part.normalized_transcription

    result = all(
        (
            has_a_normalized_transcription,
            not joins_word_right,
            not this_is_the_last_word_in_sentence_part,
        )
    )

    return result


def render_word(word: Word, buffer: StringIO, *, sep: Separators | None = None) -> StringIO:
    if sep is None:
        sep = Separators()

    to_write = sep.word_part.join(render_word_part(word_part, sep=sep) for word_part in word)

    logger.debug("Writing %s", to_write)
    buffer.write(to_write)

    return buffer


def render_word_part(word_part: WordPart, *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()
    return word_part.normalized_transcription

from __future__ import annotations

from io import StringIO
from logging import getLogger
from typing import TYPE_CHECKING

from readylog.decorators import info

from khm_renderer.corrections import CorrectionId, default_corrections
from khm_renderer.separators import Separators

if TYPE_CHECKING:
    from collections.abc import Generator

    from khm_parser.composites import Sentence, Word
    from khm_parser.elements import Head, SentencePart, WordPart
    from khm_renderer.corrections import Corrections

logger = getLogger(__name__)


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


@info
def render_tale_title(
    title: Generator[Sentence], *, sep: Separators | None = None, corrections: Corrections | None = None
) -> str:
    if sep is None:
        sep = Separators()
    if corrections is None:
        corrections = default_corrections
    buffer = StringIO()
    for num, sentence in enumerate(title, start=1):
        logger.debug("Rendering tale title Sentence %d, id: %s", num, sentence.id)
        to_write = render_sentence(sentence, corrections=corrections)
        logger.debug("Writing '%s'", to_write)
        buffer.write(to_write)

    result = buffer.getvalue()
    logger.debug("Removing '.' at the end of the title")

    return result.removesuffix(".")


def render_sentence(
    sentence: Sentence, *, sep: Separators | None = None, corrections: Corrections | None = None
) -> str:
    if sep is None:
        sep = Separators()
    if corrections is None:
        corrections = default_corrections

    buffer = StringIO()

    for num, sentence_part in enumerate(sentence, start=1):
        logger.debug("Rendering SentencePart %d, id: %s", num, sentence_part.xmlid)
        to_write = render_sentence_part(sentence_part)
        logger.debug("Writing '%s'", to_write)
        buffer.write(to_write)

        this_is_the_last_sentence_part = sentence_part.xmlid == sentence.last_part.xmlid
        should_write_separator = not this_is_the_last_sentence_part

        if should_write_separator:
            logger.debug("Writing sentence part separator")
            buffer.write(sep.sentence_part)

        logger.debug(
            "Checking corrections for SentencePart %s in dtaid %s", sentence_part.xmlid, sentence_part.DTAID
        )
        if correct := corrections.get(CorrectionId(sentence_part.DTAID, sentence_part.xmlid), False):
            buffer = correct(buffer)

    return buffer.getvalue()


def render_sentence_part(sentence_part: SentencePart, *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()

    buffer = StringIO()

    for num, word in enumerate(sentence_part, start=1):
        logger.debug("Rendering Word %d, id: %s", num, word.id)
        to_write = render_word(word)
        logger.debug("Writing '%s'", to_write)
        buffer.write(to_write)

        this_is_the_last_word_in_sentence_part = word.id == sentence_part.last_word.id
        joins_word_right = word.last_part.joins_word_right
        has_a_normalized_transcription = word.last_part.normalized_transcription

        should_write_separator = all(
            (
                has_a_normalized_transcription,
                not joins_word_right,
                not this_is_the_last_word_in_sentence_part,
            )
        )

        if should_write_separator:
            logger.debug("Writing word separator")
            buffer.write(sep.word)

    return buffer.getvalue()


def render_word(word: Word, *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()
    return sep.word_part.join(render_word_part(word_part) for word_part in word)


def render_word_part(word_part: WordPart, *, sep: Separators | None = None) -> str:
    if sep is None:
        sep = Separators()
    return word_part.normalized_transcription

from __future__ import annotations

from io import StringIO
from logging import getLogger
from typing import TYPE_CHECKING

from khm_parser.namespace import tei_namespace
from khm_parser.utils import shorten_stream_by
from khm_renderer.corrections import CorrectionId
from khm_renderer.separators import DEFAULT_TALE_NUMBER_SUFFIX

if TYPE_CHECKING:
    from collections.abc import Generator

    from khm_parser.composites import Sentence, Word
    from khm_parser.elements import Head, SentencePart, WordPart
    from khm_renderer.corrections import Corrections
    from khm_renderer.render_functions import RenderFunctions
    from khm_renderer.separators import Separators

logger = getLogger(__name__)


def render_tale_head(
    head: Head,
    buffer: StringIO,
    render_functions: RenderFunctions,
    sep: Separators,
    corrections: Corrections,
) -> StringIO:
    num_buffer = StringIO()
    num_buffer: StringIO = render_functions.render_tale_number(head.number, num_buffer, render_functions)
    number: str = num_buffer.getvalue()

    buffer.write(number)
    buffer.write(sep.tale_number_suffix)
    buffer.write(sep.sentence)
    buffer = render_functions.render_tale_title(head.title, buffer, render_functions, sep, corrections)

    return buffer


def render_tale_number(
    word_part: WordPart, buffer: StringIO, render_functions: RenderFunctions
) -> StringIO:
    number: str = render_functions.render_word_part(word_part)
    number: str = number.removesuffix(DEFAULT_TALE_NUMBER_SUFFIX)

    buffer.write(number)
    return buffer


def render_tale_title(
    title: Generator[Sentence],
    buffer: StringIO,
    render_functions: RenderFunctions,
    sep: Separators,
    corrections: Corrections,
) -> StringIO:
    for num, sentence in enumerate(title, start=1):
        logger.debug("Rendering tale title Sentence %d, id: %s", num, sentence.id)
        buffer = render_functions.render_sentence(sentence, buffer, render_functions, sep, corrections)

    logger.debug("Removing assumed '.' at the end of the title")
    shorten_stream_by(1, buffer)

    return buffer


def render_sentence(
    sentence: Sentence,
    buffer: StringIO,
    render_functions: RenderFunctions,
    sep: Separators,
    corrections: Corrections,
) -> StringIO:
    for num, sentence_part in enumerate(sentence, start=1):
        logger.debug("Rendering SentencePart %d, id: %s", num, sentence_part.xmlid)
        buffer = render_functions.render_sentence_part(sentence_part, buffer, render_functions, sep)

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
    has_space_in_tags_tail = sentence_part.tail == " "

    parent = sentence_part.getparent()
    parent_is_highlight = parent.tag == tei_namespace("hi")
    parent_has_space_in_tail = parent.tail == " "
    parent_is_line = parent.tag == tei_namespace("l")
    parent_has_eleven_spaces_in_tail = parent.tail == "           "

    result = any(
        (
            has_space_in_tags_tail,
            not has_space_in_tags_tail and parent_is_highlight and parent_has_space_in_tail,
            not has_space_in_tags_tail and parent_is_line and parent_has_eleven_spaces_in_tail,
        )
    )

    return result


def render_sentence_part(
    sentence_part: SentencePart, buffer: StringIO, render_functions: RenderFunctions, sep: Separators
) -> StringIO:
    for num, word in enumerate(sentence_part, start=1):
        logger.debug("Rendering Word %d, id: %s", num, word.id)
        buffer = render_functions.render_word(word, buffer, render_functions, sep)

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


def render_word(
    word: Word, buffer: StringIO, render_functions: RenderFunctions, sep: Separators
) -> StringIO:
    to_write = sep.word_part.join(render_functions.render_word_part(word_part) for word_part in word)

    logger.debug("Writing %s", to_write)
    buffer.write(to_write)

    return buffer


def get_normalized_transcription_of_word_part(word_part: WordPart) -> str:
    return word_part.normalized_transcription

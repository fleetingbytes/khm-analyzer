from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from io import StringIO

    from khm_parser.composites import Sentence
    from khm_parser.elements import WordPart
    from khm_parser.elements.sentence_part import SentencePart
    from khm_renderer.corrections import Corrections
    from khm_renderer.render_functions import RenderFunctions
    from khm_renderer.separators import Separators


def get_first_letter_of_word_part(word_part: WordPart) -> str:
    return next(iter(word_part.normalized_transcription), "")


def render_sentence_part_xmlid(
    sentence_part: SentencePart, buffer: StringIO, render_functions: RenderFunctions, sep: Separators
) -> StringIO:
    buffer.write(sentence_part.xmlid)
    return buffer


def render_sentence_as_s(
    sentence: Sentence,
    buffer: StringIO,
    render_functions: RenderFunctions,
    sep: Separators,
    corr: Corrections,
) -> StringIO:
    if sentence.has_multiple_parts:
        buffer.write("S")
    else:
        buffer.write("s")
    return buffer

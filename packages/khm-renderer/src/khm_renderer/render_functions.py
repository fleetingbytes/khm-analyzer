from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from khm_renderer.standard_render_functions import (
    get_normalized_transcription_of_word_part,
    render_sentence,
    render_sentence_part,
    render_tale_head,
    render_tale_number,
    render_tale_title,
    render_word,
)

if TYPE_CHECKING:
    from collections.abc import Callable


@dataclass(slots=True)
class RenderFunctions:
    render_tale_head: Callable = render_tale_head
    render_tale_number: Callable = render_tale_number
    render_tale_title: Callable = render_tale_title
    render_sentence: Callable = render_sentence
    render_sentence_part: Callable = render_sentence_part
    render_word: Callable = render_word
    render_word_part: Callable = get_normalized_transcription_of_word_part

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from khm_renderer.render import (
    render_sentence,
    render_sentence_part,
    render_word,
    render_word_part,
)

if TYPE_CHECKING:
    from collections.abc import Callable


@dataclass(slots=True)
class Renderers:
    word_part: Callable = render_word_part
    word: Callable = render_word
    sentence_part: Callable = render_sentence_part
    sentence: Callable = render_sentence

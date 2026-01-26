from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from khm_parser.elements import Head
    from khm_renderer.corrections import Corrections
    from khm_renderer.separators import Separators


def render_head(
    head: Head, separators: Separators | None = None, corrections: Corrections | None = None
) -> str:
    return ""

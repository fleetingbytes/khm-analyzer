from __future__ import annotations

from typing import TYPE_CHECKING

from khm_analyzer.setup_logging import setup_logging
from khm_renderer.separators import Separators

if TYPE_CHECKING:
    from behave.runner import Context

setup_logging()


def before_all(context: Context) -> None:
    context.output = None
    context.sep = Separators()

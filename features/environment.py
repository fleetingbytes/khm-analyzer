from __future__ import annotations

from typing import TYPE_CHECKING

from khm_analyzer.setup_logging import setup_logging
from khm_renderer.renderers import Renderers
from khm_renderer.separators import Separators

if TYPE_CHECKING:
    from behave.runner import Context, Scenario

setup_logging()


def before_scenario(context: Context, scenario: Scenario) -> None:
    context.output = None
    context.sep = Separators()
    context.renderers = Renderers()

from __future__ import annotations

from io import StringIO
from typing import TYPE_CHECKING

from khm_analyzer.setup_logging import setup_logging
from khm_renderer import KhmRenderer

if TYPE_CHECKING:
    from behave.runner import Context, Scenario

setup_logging()


def before_scenario(context: Context, scenario: Scenario) -> None:
    context.buffer = StringIO()
    context.output = None
    context.renderer = KhmRenderer()

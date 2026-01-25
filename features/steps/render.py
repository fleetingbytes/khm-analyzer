from __future__ import annotations

from typing import TYPE_CHECKING

from behave import register_type, when
from behave4khm_analyzer.matching_types import MATCHING_TYPES
from behave4khm_analyzer.utils import get_source_path

from khm_analyzer.api import render_title

if TYPE_CHECKING:
    from behave.runner import Context
    from khm_enums import Edition, Volume


register_type(**MATCHING_TYPES)


@when("I render the title of the tale {tale:d} from edition {edition:Edition}, volume {volume:Volume}")
def render_title_of_tale(context: Context, tale: int, edition: Edition, volume: Volume) -> None:
    path = get_source_path(context.source_directory, edition, volume)
    with path.open(mode="rb") as file:
        context.output: str = render_title(file, tale)

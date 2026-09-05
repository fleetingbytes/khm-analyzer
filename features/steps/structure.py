from __future__ import annotations

from typing import TYPE_CHECKING

from behave import given, when

from behave4khm_analyzer.utils import get_source_path, read_string_buffer
from khm_parser import get_all_fairy_tales
from khm_parser.utils import shorten_stream_by

if TYPE_CHECKING:
    from behave.runner import Context

    from khm_enums import Edition, Volume


@given("I parse all tales in edition {edition:Edition}, volume {volume:Volume}")
def parse_ed_x_vol_y(context: Context, edition: Edition, volume: Volume) -> None:
    source_directory = context.source_directory
    path = get_source_path(source_directory, edition, volume)
    context.tales = get_all_fairy_tales(path)


@when("I render the numbers of all the tales")
def render_numbers_of_all_tales(context: Context) -> None:
    tales = context.tales
    renderer = context.renderer
    buffer = context.buffer

    for tale in tales:
        number = tale.number
        buffer = renderer.render_tale_number(number, buffer)
        buffer.write(renderer.sep.word)

    shorten_stream_by(len(renderer.sep.word), buffer)
    context.output: str = read_string_buffer(buffer)

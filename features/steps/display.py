from __future__ import annotations

from typing import TYPE_CHECKING

from behave import given, register_type, then, when
from behave4khm_analyzer.matching_types import MATCHING_TYPES
from behave4khm_analyzer.utils import check_presence_of_source_files, get_source_path

from khm_analyzer.api import render_tale

if TYPE_CHECKING:
    from pathlib import Path

    from behave.runner import Context

    from khm_analyzer.enums import Edition, Volume


register_type(**MATCHING_TYPES)


@given("source documents in directory {directory:Path}")
def source_documents_in_directory(context: Context, directory: Path) -> None:
    check_presence_of_source_files(directory)
    context.source_directory = directory


@when("I display the tale {tale:d} from edition {edition:Edition}, volume {volume:Volume}")
def display_tale(context: Context, tale: int, edition: Edition, volume: Volume) -> None:
    path = get_source_path(context.source_directory, edition, volume)
    show_number: bool = getattr(context, "show_tale_number", False)
    show_title: bool = getattr(context, "show_tale_title", False)
    with path.open(mode="rb") as file:
        context.displayed_tale: str = render_tale(
            file, tale, show_number=show_number, show_title=show_title
        )


@when("I select the option to show the tale number")
def display_tale_number(context: Context) -> None:
    context.show_tale_number = True


@when("I select the option to show the tale title")
def display_tale_title(context: Context) -> None:
    context.show_tale_title = True


@then("the output starts with {out:Rest}")
def output_starts_with(context: Context, out: str) -> None:
    assert context.displayed_tale.startswith(out), (
        f'expected the displayed tale to start with "{out}", '
        f'but found "{context.displayed_tale[: len(out)]}"'
    )

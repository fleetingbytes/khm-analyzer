from __future__ import annotations

from itertools import product
from pathlib import Path
from typing import TYPE_CHECKING, Any

from behave import given, register_type, then, use_step_matcher, when
from behave.api.pending_step import StepNotImplementedError

from khm_analyzer.enums import Edition, Volume

if TYPE_CHECKING:
    from collections.abc import Callable

    from behave.runner import Context


def parse_to_path(text: str) -> Path:
    return Path(text.strip())


def parse_to_edition(n: str) -> Edition:
    return Edition(int(n))


def parse_to_volume(n: str) -> Volume:
    return Volume(int(n))


def parse_rest_of_line(s: str) -> str:
    return s.strip()


def check_presence_of_source_files(directory: Path) -> None:
    file_names_with_parent_dir = map(lambda path: path.name, directory.glob("*.xml"))
    file_names = tuple(map(str, file_names_with_parent_dir))

    for ed, vol in product(Edition, Volume):
        assert f"khm-ed{ed.value}-vol{vol.value}.xml" in file_names


use_step_matcher("parse")

MATCHING_TYPES: dict[str, Callable[[str], Any]] = dict(
    Path=parse_to_path,
    Edition=parse_to_edition,
    Volume=parse_to_volume,
    Rest=parse_rest_of_line,
)

register_type(**MATCHING_TYPES)


@given("source documents in directory {directory:Path}")
def source_docuents_in_directory(context: Context, directory: Path) -> None:
    check_presence_of_source_files(directory)
    context.source_directory = directory


@when("I display the tale {tale:d} from edition {edition:Edition}, volume {volume:Volume}")
def display_tale(context: Context, tale: int, edition: Edition, volume: Volume) -> None:
    raise StepNotImplementedError


@then("the output starts with {out:Rest}")
def output_starts_with(context: Context, out: str) -> None:
    raise StepNotImplementedError

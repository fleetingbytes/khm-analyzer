from __future__ import annotations

from typing import TYPE_CHECKING

from behave import given, register_type, then, when

from behave4khm_analyzer.matching_types import MATCHING_TYPES
from behave4khm_analyzer.utils import check_presence_of_source_files, get_source_path
from khm_parser import parse_tale
from khm_renderer import render_tale_head, render_tale_number, render_tale_title

if TYPE_CHECKING:
    from collections.abc import Generator
    from pathlib import Path

    from behave.runner import Context

    from khm_enums import Edition, Volume
    from khm_parser.composites import Sentence
    from khm_parser.elements import Head, Tale, WordPart


register_type(**MATCHING_TYPES)


@given("source documents in directory {directory:Path}")
def source_documents_in_directory(context: Context, directory: Path) -> None:
    check_presence_of_source_files(directory)
    context.source_directory = directory


@given("I parse the tale {tale:d} from edition {edition:Edition}, volume {volume:Volume}")
def parse_tale_impl(context: Context, tale: int, edition: Edition, volume: Volume) -> None:
    path = get_source_path(context.source_directory, edition, volume)
    context.tale: Tale = parse_tale(path, tale)


@when("I render the number of the tale")
def render_number_of_tale(context: Context) -> None:
    tale: Tale = context.tale
    number: WordPart = tale.number
    context.output: str = render_tale_number(number)


@when("I render the title of the tale")
def render_title_of_tale(context: Context) -> None:
    tale: Tale = context.tale
    title: Generator[Sentence] = tale.title
    context.output: str = render_tale_title(title)


@when("I render the head of the tale")
def render_head_of_tale(context: Context) -> None:
    tale: Tale = context.tale
    head: Head = tale.head
    context.output: str = render_tale_head(head)


@then("the output is {out:Rest}")
def output_starts_with(context: Context, out: str) -> None:
    assert context.output == out, f'expected the output to be "{out}", but found "{context.output}"'

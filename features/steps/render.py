from __future__ import annotations

from io import StringIO
from typing import TYPE_CHECKING

from behave import given, register_type, then, when

from behave4khm_analyzer.matching_types import MATCHING_TYPES
from behave4khm_analyzer.utils import (
    check_presence_of_source_files,
    find_and_render_word,
    find_and_render_word_part,
    get_source_path,
    read_string_buffer,
)
from khm_parser import parse_tale
from khm_renderer import (
    render_tale_head,
    render_tale_number,
    render_tale_title,
)

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


@given("the word part separator {word_part_sep}")
def set_word_part_sep(context: Context, word_part_sep: str) -> None:
    context.sep.word_part = word_part_sep


@when("I render the number of the tale")
def render_number_of_tale(context: Context) -> None:
    tale: Tale = context.tale
    number: WordPart = tale.number
    context.output: str = render_tale_number(number)


@when("I render the title of the tale")
def render_title_of_tale(context: Context) -> None:
    tale: Tale = context.tale
    title: Generator[Sentence] = tale.title
    buffer = StringIO()

    buffer = render_tale_title(title, buffer)
    context.output: str = read_string_buffer(buffer)


@when("I render the head of the tale")
def render_head_of_tale(context: Context) -> None:
    tale: Tale = context.tale
    head: Head = tale.head
    buffer = StringIO()

    buffer = render_tale_head(head, buffer)
    context.output: str = read_string_buffer(buffer)


@then("the output is {out:Rest}")
def output_is(context: Context, out: str) -> None:
    assert context.output == out, f"expected the output to be {out!r}, but found {context.output!r}"


@then("the output is ")
def output_is_empty(context: Context) -> None:
    assert context.output == "", f"expected the output to be an empty string, but found {context.output!r}"


@when("I render the word part {word_part_id}")
def render_word_part_impl(context: Context, word_part_id: str) -> None:
    tale: Tale = context.tale
    context.output: str | None = find_and_render_word_part(tale, word_part_id)


@when("I render the word {word_id}")
def render_word_impl(context: Context, word_id: str) -> None:
    tale: Tale = context.tale
    buffer = StringIO()
    sep = context.sep

    buffer = find_and_render_word(tale, buffer, word_id, sep=sep)
    context.output = read_string_buffer(buffer)

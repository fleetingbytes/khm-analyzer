from __future__ import annotations

from typing import TYPE_CHECKING

from behave import given, register_type, then, when

from behave4khm_analyzer.custom_render_functions import (
    get_first_letter_of_word_part,
    render_sentence_as_s,
    render_sentence_part_xmlid,
)
from behave4khm_analyzer.matching_types import MATCHING_TYPES
from behave4khm_analyzer.utils import (
    check_presence_of_source_files,
    find_and_render_sentence,
    find_and_render_sentence_part,
    find_and_render_word,
    find_and_render_word_part,
    get_source_path,
    read_string_buffer,
)
from khm_parser import parse_tale

if TYPE_CHECKING:
    from collections.abc import Generator
    from pathlib import Path

    from behave.runner import Context

    from khm_enums import Edition, Volume
    from khm_parser.composites import Sentence
    from khm_parser.elements import Head, Tale, WordPart
    from khm_renderer import KhmRenderer


register_type(**MATCHING_TYPES)


@given("source documents in directory {directory:Path}")
def source_documents_in_directory(context: Context, directory: Path) -> None:
    check_presence_of_source_files(directory)
    context.source_directory = directory


@given("I parse the tale {tale:d} from edition {edition:Edition}, volume {volume:Volume}")
def parse_tale_impl(context: Context, tale: int, edition: Edition, volume: Volume) -> None:
    source_directory = context.source_directory
    path = get_source_path(source_directory, edition, volume)
    context.tale: Tale = parse_tale(path, tale)


@given("the word part separator {word_part_sep}")
def set_word_part_sep(context: Context, word_part_sep: str) -> None:
    context.renderer.sep.word_part = word_part_sep


@given("the word separator {word_sep}")
def set_word_sep(context: Context, word_sep: str) -> None:
    context.renderer.sep.word = word_sep


@given("the word part renderer renders only the first letter")
def set_word_renderer_for_first_letter(context: Context) -> None:
    context.renderer.renderers.render_word_part = get_first_letter_of_word_part


@given("the sentece part renderer renders only the xmlid")
def set_sentence_renderer_for_xmlid(context: Context) -> None:
    context.renderer.renderers.render_sentence_part = render_sentence_part_xmlid


@given("the sentece renderer s_or_S")
def set_sentence_renderer_s_or_s(context: Context) -> None:
    context.renderer.renderers.render_sentence = render_sentence_as_s


@when("I render the number of the tale")
def render_number_of_tale(context: Context) -> None:
    tale: Tale = context.tale
    tale_number: WordPart = tale.number
    renderer: KhmRenderer = context.renderer
    buffer = context.buffer

    buffer = renderer.render_tale_number(tale_number, buffer)
    context.output: str = read_string_buffer(buffer)


@when("I render the title of the tale")
def render_title_of_tale(context: Context) -> None:
    tale: Tale = context.tale
    title: Generator[Sentence] = tale.title
    renderer: KhmRenderer = context.renderer
    buffer = context.buffer

    buffer = renderer.render_tale_title(title, buffer)
    context.output: str = read_string_buffer(buffer)


@when("I render the head of the tale")
def render_head_of_tale(context: Context) -> None:
    tale: Tale = context.tale
    head: Head = tale.head
    renderer: KhmRenderer = context.renderer
    buffer = context.buffer

    buffer = renderer.render_tale_head(head, buffer)
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
    renderer: KhmRenderer = context.renderer
    buffer = context.buffer

    buffer = find_and_render_word_part(tale, word_part_id, renderer, buffer)
    context.output: str = read_string_buffer(buffer)


@when("I render the word {word_id}")
def render_word_impl(context: Context, word_id: str) -> None:
    tale: Tale = context.tale
    renderer: KhmRenderer = context.renderer
    buffer = context.buffer

    buffer = find_and_render_word(tale, word_id, renderer, buffer)
    context.output = read_string_buffer(buffer)


@when("I render the sentence part {sentence_part_id}")
def render_sentence_part_impl(context: Context, sentence_part_id: str) -> None:
    tale: Tale = context.tale
    renderer: KhmRenderer = context.renderer
    buffer = context.buffer

    buffer = find_and_render_sentence_part(tale, sentence_part_id, renderer, buffer)
    context.output = read_string_buffer(buffer)


@when("I render the sentence {sentence_id}")
def render_sentence_impl(context: Context, sentence_id: str) -> None:
    tale: Tale = context.tale
    renderer: KhmRenderer = context.renderer
    buffer = context.buffer

    buffer = find_and_render_sentence(tale, sentence_id, renderer, buffer)
    context.output = read_string_buffer(buffer)

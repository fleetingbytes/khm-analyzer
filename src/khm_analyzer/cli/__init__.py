from __future__ import annotations

from logging import getLogger
from pathlib import Path
from typing import TYPE_CHECKING

from click import File, argument, group, option, version_option
from click import Path as ClickPath
from readylog.decorators import debug_in

from khm_analyzer.cli.callbacks import to_edition, to_volume
from khm_analyzer.cli.display import display
from khm_analyzer.cli.download_all_sources import download_all_sources as download_all_sources
from khm_analyzer.cli.download_source import download_source as download_source
from khm_analyzer.cli.setup_logging import setup_logging
from khm_analyzer.cli.validate import validate

if TYPE_CHECKING:
    from khm_analyzer.enums import Edition, Volume

MAX_HELP_CONTENT_WIDTH = 108

logger = getLogger(__name__)
setup_logging()


@group(
    context_settings={"show_default": True, "max_content_width": MAX_HELP_CONTENT_WIDTH},
)
@version_option()
def cli() -> None:
    pass


@cli.command("display", short_help="show text of tales")
@argument("source_file", type=File())
@argument("tale", type=int)
@option("-n", "--include-tale-number", is_flag=True)
@option("-t", "--include-tale-title", is_flag=True)
@option("-s", "--one-sentence-per-line", is_flag=True)
def display_cli(
    source_file: File,
    tale: int,
    include_tale_number: bool,
    include_tale_title: bool,
    one_sentence_per_line: bool,
) -> None:
    display(source_file, tale, include_tale_number, include_tale_title, one_sentence_per_line)


@cli.command("validate", short_help="validate source xml")
@argument("paths", type=File(), required=True, nargs=-1)
def validate_cli(paths: tuple[File]) -> None:
    validate(paths)


@cli.command("download-source", short_help="download a source document")
@argument("edition", type=int, callback=to_edition)
@argument("volume", type=int, callback=to_volume)
@argument("file_path", type=ClickPath(allow_dash=True, path_type=Path))
def download_source_cli(edition: Edition, volume: Volume, file_path: Path) -> None:
    download_source(edition, volume, file_path)


@cli.command("download-all-sources", short_help="download all source documents")
@argument("directory", type=ClickPath(path_type=Path))
def download_all_sources_cli(directory: Path) -> None:
    download_all_sources(directory)


@debug_in
def run() -> None:
    cli()

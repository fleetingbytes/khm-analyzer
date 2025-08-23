from argparse import ArgumentParser, FileType
from pathlib import Path
from .display import display
from .validate import validate
from .download_source import download_source
from .download_all_sources import download_all_sources
from logging import getLogger
from logging.config import dictConfig as configure_logging
from ..logging_conf import logging_configuration

configure_logging(logging_configuration)

logger = getLogger(__name__)

arg_parser = ArgumentParser(
    prog="khm-analyzer",
    description="Parses linguistically annotated editions of Grimm's Fairy Tales",
)


subparsers = arg_parser.add_subparsers(title="subcommands", help="sub-command help", required=True)
display_parser = subparsers.add_parser("display", help="show text of tales")
display_parser.set_defaults(subcommand_function=display)
validate_parser = subparsers.add_parser("validate", help="validate source xml")
validate_parser.set_defaults(subcommand_function=validate)
download_source_parser = subparsers.add_parser("download-source", help="download a source document")
download_source_parser.set_defaults(subcommand_function=download_source)
download_all_sources_parser = subparsers.add_parser(
    "download-all-sources", help="download all source documents"
)
download_all_sources_parser.set_defaults(subcommand_function=download_all_sources)

display_parser.add_argument("source_file", type=FileType("r", encoding="UTF-8"))
display_parser.add_argument("tale", type=int)
display_parser.add_argument("-n", "--include-tale-number", action="store_true")
display_parser.add_argument("-t", "--include-tale-title", action="store_true")
display_parser.add_argument("-s", "--one-sentence-per-line", action="store_true")

validate_parser.add_argument(
    "-d",
    "--directory",
    action="store_true",
    help="validate all files in one or more directories",
)
validate_parser.add_argument(
    "-c", "--try-to-correct", action="store_true", help="try to correct invalid XML"
)
validate_parser.add_argument("path", type=Path, nargs="+", help="validate one or more files")

download_source_parser.add_argument("edition", type=int, help="edition number (1-7)")
download_source_parser.add_argument("volume", type=int, help="volume number (1-2)")
download_source_parser.add_argument("file", type=Path, help="output file")

download_all_sources_parser.add_argument(
    "path_pattern",
    type=Path,
    help='path pattern, e.g. "~/grimm/khm.xml", "-edX-volY" will be attached to the file stem.',
)


def run() -> None:
    logger.debug("Parsing arguments")
    args = arg_parser.parse_args()
    args.subcommand_function(args)

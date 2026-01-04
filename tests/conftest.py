from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from argparse import ArgumentParser

CLI_FLAG_FOR_XML_DOWNLOAD = "--download-xml-source"


def pytest_addoption(parser: ArgumentParser):
    parser.addoption(
        CLI_FLAG_FOR_XML_DOWNLOAD,
        action="store_true",
        default=False,
        help="Run expensive XML download and validity tests",
    )

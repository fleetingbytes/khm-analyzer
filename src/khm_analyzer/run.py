from importlib.metadata import version as get_version
from logging import getLogger
from sys import modules

from khm_analyzer.setup_logging import setup_logging
from khm_cli.cli import cli

logger = getLogger(__name__)
setup_logging()


def run() -> None:
    app_name = next(iter(modules[__name__].__spec__.parent.split(".")))
    version = get_version(app_name)
    logger.debug("Running %s version %s", app_name, version)
    cli()

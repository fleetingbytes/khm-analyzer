from argparse import Namespace
from ..validation import validate_directories, validate_paths
from warnings import catch_warnings
from logging import getLogger

logger = getLogger(__name__)


def validate(args: Namespace) -> None:
    logger.debug("running validate")
    correction_wanted = args.try_to_correct
    with catch_warnings(record=True) as w:
        if args.directory:
            validate_directories(args.path, correction_wanted)
        else:
            validate_paths(args.path, correction_wanted)
    for warning in w:
        print(warning.message)

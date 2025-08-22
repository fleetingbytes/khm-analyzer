from functools import wraps
from io import IOBase, TextIOWrapper
from os import SEEK_SET
from pathlib import Path
from logging import getLogger, DEBUG


logger = getLogger(__name__)


def set_stream_position_to_the_start(buffer: IOBase) -> None:
    logger.debug("Position reset to start in %s", get_file_name_from_buffer(buffer))
    _ = buffer.seek(0, SEEK_SET)


def get_file_name_from_buffer(buffer: TextIOWrapper) -> str:
    try:
        return Path(buffer.name).name
    except AttributeError:
        return f"{buffer} Id: {id(buffer)}"


def log_io(level: int = DEBUG, enter: bool = False, exit: bool = False):
    """
    Decorator factory that logs function input arguments and return values
    at the specified logging level.

    Usage:
        debug = @log_io(logging.DEBUG, enter=True, exit=True)

        @debug
        def my_func(...):
            ...
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if enter:
                logger.log(
                    level,
                    "Calling %s with args=%s, kwargs=%s",
                    func.__name__,
                    args,
                    kwargs,
                    stacklevel=2,
                )
            result = func(*args, **kwargs)
            if exit:
                logger.log(level, "%s returned %r", func.__name__, result, stacklevel=2)
            return result

        return wrapper

    return decorator


debug = log_io(DEBUG, enter=True, exit=True)
debug_in = log_io(DEBUG, enter=True)
debug_out = log_io(DEBUG, exit=True)

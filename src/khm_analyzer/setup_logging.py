from logging.config import dictConfig as configure_logging
from pathlib import Path

from platformdirs import user_log_dir
from readylog import create_dict_config


def setup_logging() -> None:
    app_name = "khm_analyzer"
    author = "fleetingbytes"

    log_dir = Path(user_log_dir(app_name, author))
    log_dir.mkdir(parents=True, exist_ok=True)

    logging_config = create_dict_config(log_dir / "debug.log", app_name)
    configure_logging(logging_config)

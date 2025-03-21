import datetime
import logging
import sys

import structlog

from aiogram_bot import models
from aiogram_bot.data import config


def setup_logger() -> structlog.typing.FilteringBoundLogger:
    # logging.basicConfig(
    #     level=config.LOGGING_LEVEL,
    #     stream=None,
    # )
    # logFormatter = logging.Formatter(fmt=' %(name)s :: %(levelname)-8s :: %(message)s')
    log: structlog.typing.FilteringBoundLogger = structlog.get_logger(
        structlog.stdlib.BoundLogger
    )
    shared_processors: list[structlog.typing.Processor] = [
        structlog.processors.add_log_level
    ]
    if sys.stderr.isatty() or True:
        # Pretty printing when we run in a terminal session.
        # Automatically prints pretty tracebacks when "rich" is installed
        processors = shared_processors + [

            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=False),
            structlog.dev.ConsoleRenderer(),
        ]
    else:
        # Print JSON when we run, e.g., in a Docker container.
        # Also print structured tracebacks.
        processors = shared_processors + [
            structlog.processors.TimeStamper(fmt=None, utc=True),
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(serializer=models.base.orjson_dumps),
        ]
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(config.LOGGING_LEVEL),
    )
    return log


"""Implements the "magic" to create `logging` records for the caller."""

import sys
import logging
import inspect

from . import helpers, state


def create_logger_record(level, message, *args, exc_info=None, **kwargs):
    if not state.initialized and 'pytest' not in sys.modules:
        helpers.init()

    frame, filename, lineno, *_ = inspect.stack()[3]
    module = inspect.getmodule(frame)

    logger = logging.getLogger()
    if not logger.isEnabledFor(level):
        return

    helpers.install_additional_formats(logger)

    record = logger.makeRecord(
        module.__name__,
        level,
        fn=filename,
        lno=lineno,
        msg=message,
        args=args,
        exc_info=exc_info,
        extra=kwargs,
        sinfo=None,
    )
    logger.handle(record)

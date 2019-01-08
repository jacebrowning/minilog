"""Implements the "magic" to create `logging` records for the caller."""

import inspect
import logging
import sys

from . import helpers, state


def create_logger_record(level, message, *args, exc_info=None, **kwargs):
    if 'pytest' in sys.modules:
        root = logging.getLogger()
        helpers.install_additional_formats(root)
    elif not state.initialized:
        helpers.init()

    frame, filename, lineno, *_ = inspect.stack(0)[3]

    module = inspect.getmodule(frame)

    logger = logging.getLogger(module.__name__)
    if not logger.isEnabledFor(level):
        return

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

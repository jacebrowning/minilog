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

    frame = inspect.currentframe().f_back.f_back.f_back

    module_name = kwargs.pop('module_name', frame.f_globals['__name__'])
    parent_module_name = module_name.split('.')[0]

    logger = logging.getLogger(module_name)
    if not logger.level:
        parent_logger = logging.getLogger(parent_module_name)
        logger.level = parent_logger.level
    if not logger.level:
        logger.level = state.default_level

    if not logger.isEnabledFor(level):
        return False

    record = logger.makeRecord(
        module_name,
        level,
        fn=frame.f_globals['__file__'],
        lno=frame.f_lineno,
        msg=message,
        args=args,
        exc_info=exc_info,
        extra=kwargs,
        sinfo=None,
    )
    logger.handle(record)
    return True

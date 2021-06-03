"""Implements the "magic" to create `logging` records for the caller."""

import inspect
import logging
from typing import Dict, Tuple

from . import state


def create_logger_record(
    level, message, *args, name: str = '', exc_info=None, **kwargs
) -> bool:
    frame = inspect.currentframe().f_back.f_back.f_back  # type: ignore

    name, parent_name = parse_name(name, frame.f_globals)
    if parent_name in state.silenced:
        return False

    logger = get_logger(name, parent_name)
    if not logger.isEnabledFor(level):
        return False

    record = logger.makeRecord(
        name,
        level,
        fn=parse_fn(frame.f_globals),
        lno=frame.f_lineno,
        msg=message,
        args=args,
        exc_info=exc_info,
        extra=kwargs,
        sinfo=None,
    )
    logger.handle(record)
    return True


def parse_fn(frame_info: Dict) -> str:
    return frame_info.get('__file__', 'interactive')


def parse_name(custom_name: str, frame_info: Dict) -> Tuple[str, str]:
    module_name = custom_name or frame_info['__name__']
    if module_name == '__main__':
        try:
            module_name = frame_info['__file__'].split('.')[0].replace('/', '.')
        except KeyError:
            module_name = 'interactive'
    parent_module_name = module_name.split('.')[0]
    return module_name, parent_module_name


def get_logger(name: str, parent_name: str):
    logger = logging.getLogger(name)
    if not logger.level:
        parent_logger = logging.getLogger(parent_name)
        logger.level = parent_logger.level
    if not logger.level:
        logger.level = logging.root.level
    return logger

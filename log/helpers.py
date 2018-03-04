"""Wrappers to eliminate boilerplate `logging` activities."""

import logging


DEFAULT_LEVEL = logging.INFO
DEFAULT_FORMAT = "%(levelname)s: %(name)s: %(message)s"

initialized = False


def init(**kwargs):
    custom_format = kwargs.get('format')
    kwargs['level'] = kwargs.get('level', DEFAULT_LEVEL)
    kwargs['format'] = kwargs.get('format', DEFAULT_FORMAT)
    logging.basicConfig(**kwargs)
    if custom_format:
        formatter = logging.Formatter(custom_format)
        for handler in logging.root.handlers:
            handler.setFormatter(formatter)

    global initialized
    initialized = True

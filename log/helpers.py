"""Wrappers to eliminate boilerplate `logging` activities."""

import logging


DEFAULT_LEVEL = logging.INFO
DEFAULT_FORMAT = "%(levelname)s: %(name)s: %(message)s"

initialized = False


def init(*, reset=False, debug=False, **kwargs):
    if reset:
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    custom_format = kwargs.get('format')
    default_level = logging.DEBUG if debug else DEFAULT_LEVEL

    kwargs['level'] = kwargs.get('level', default_level)
    kwargs['format'] = kwargs.get('format', DEFAULT_FORMAT)
    logging.basicConfig(**kwargs)

    if custom_format:
        formatter = logging.Formatter(custom_format)
        for handler in logging.root.handlers:
            handler.setFormatter(formatter)

    global initialized
    initialized = True


def silence(*names, allow_info=False, allow_warning=False, allow_error=False):
    if allow_info:
        level = logging.INFO
    elif allow_warning:
        level = logging.WARNING
    elif allow_error:
        level = logging.ERROR
    else:
        level = logging.CRITICAL

    for name in names:
        logging.getLogger(name).setLevel(level)

"""Wrappers to eliminate boilerplate `logging` activities."""

import logging
import warnings
from importlib import reload

from . import state
from .filters import relpath_format_filter

VERBOSITY_TO_LEVEL = {
    0: logging.ERROR,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG,
}


def reset():
    logging.shutdown()
    reload(logging)


def init(*, debug=False, verbosity=None, **kwargs):
    if 'reset' in kwargs:  # pragma: no cover
        warnings.warn(
            (
                "'reset' option will be removed in the next major version."
                " Use 'log.reset()' instead."
            ),
            DeprecationWarning,
        )
        should_reset = kwargs.pop('reset')
        if should_reset:
            reset()

    custom_format = kwargs.get('format')
    if debug:
        state.default_level = logging.DEBUG
    elif verbosity is not None:
        state.default_level = VERBOSITY_TO_LEVEL[verbosity]

    kwargs['level'] = kwargs.get('level', state.default_level)
    kwargs['format'] = kwargs.get('format', state.default_format)
    logging.basicConfig(**kwargs)

    if custom_format:
        formatter = logging.Formatter(
            fmt=custom_format,
            datefmt=kwargs.get('datefmt'),
            style=kwargs.get('style', '%'),
        )
        for handler in logging.root.handlers:
            handler.setFormatter(formatter)

    install_additional_formats(logging.root)

    state.initialized = True


def install_additional_formats(logger):
    for handler in logger.handlers:
        handler.addFilter(relpath_format_filter)


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

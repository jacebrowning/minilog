"""Wrappers to eliminate boilerplate `logging` activities."""

import logging
import sys
from importlib import reload

from . import filters, settings, state

__all__ = ["reset", "init", "silence"]

VERBOSITY_TO_LEVEL = {
    0: logging.ERROR,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG,
}


def reset():
    logging.shutdown()
    reload(logging)
    state.initialized = False
    state.silenced.clear()


def init(*, debug=False, verbosity=None, **kwargs):
    if debug:
        settings.DEFAULT_LEVEL = logging.DEBUG
    elif verbosity is not None:
        try:
            settings.DEFAULT_LEVEL = VERBOSITY_TO_LEVEL[verbosity]
        except KeyError:
            settings.DEFAULT_LEVEL = logging.DEBUG

    kwargs["level"] = kwargs.get("level", settings.DEFAULT_LEVEL)
    kwargs["format"] = kwargs.get("format", settings.DEFAULT_FORMAT)
    logging.basicConfig(**kwargs)

    custom_format = kwargs.get("format")
    if custom_format:
        formatter = logging.Formatter(
            fmt=custom_format,
            datefmt=kwargs.get("datefmt"),
            style=kwargs.get("style", "%"),
        )
        for handler in logging.root.handlers:
            handler.setFormatter(formatter)

    filters.install(logging.root)
    state.initialized = True


def silence(*names, allow_info=False, allow_warning=False, allow_error=False):
    if not state.initialized:
        if "pytest" in sys.modules:
            filters.install(logging.root)
        else:
            init()

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
        state.silenced.add(name)

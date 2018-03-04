"""Replicates some of the `logging.Logger` API."""

import logging

from . import utils


def log(level, message, *args, **kwargs):
    utils.create_logger_record(level, message, *args, **kwargs)


def debug(message, *args, **kwargs):
    log(logging.DEBUG, message, *args, **kwargs)


def info(message, *args, **kwargs):
    log(logging.INFO, message, *args, **kwargs)


def warning(message, *args, **kwargs):
    log(logging.WARNING, message, *args, **kwargs)


def error(message, *args, **kwargs):
    log(logging.ERROR, message, *args, **kwargs)


def critical(message, *args, **kwargs):
    log(logging.CRITICAL, message, *args, **kwargs)


def exception(*args, **kwargs):  # pylint: disable=unused-argument
    raise NotImplementedError

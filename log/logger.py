"""Replicates some of the `logging.Logger` API."""

import logging
import sys

from . import utils


__all__ = ['log', 'debug', 'info', 'warning', 'error', 'critical', 'exception']


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


def exception(message, *args, **kwargs):
    kwargs['exc_info'] = kwargs.get('exc_info', sys.exc_info())
    log(logging.ERROR, message, *args, **kwargs)

import inspect
import logging

__all__ = [
    'debug',
    'info',
    'warn', 'warning',
    'error',
    'critical',

    # 'exception',

    'log',
]


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


def log(level, message, *args, **kwargs):
    _log(level, message, *args, **kwargs)


# def exception(*args, **kwargs):
#     return log(logging.DEBUG, *args, **kwargs)


warn = warning


def _log(level, message, *args, **kwargs):
    frame_info = inspect.stack()[3]
    module = inspect.getmodule(frame_info.frame)
    logger = logging.getLogger()
    record = logger.makeRecord(
        module.__name__,
        level,
        fn=frame_info.filename,
        lno=frame_info.lineno,
        msg=message,
        args=args,
        exc_info=None,
        extra=kwargs,
        sinfo=None,
    )
    logger.handle(record)

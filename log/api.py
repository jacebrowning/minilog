import inspect
import logging


__all__ = [
    'init',

    'd', 'debug',
    'i', 'info',
    'w', 'warn', 'warning',
    'e', 'error',
    'critical',

    # 'exception',

    'log',
]


def init(**kwargs):
    logging.basicConfig(**kwargs)
    if 'format' in kwargs:
        formatter = logging.Formatter(kwargs['format'])
        for handler in logging.root.handlers:
            handler.setFormatter(formatter)


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


d = debug
i = info
w = warn = warning
e = error


def _log(level, message, *args, **kwargs):
    frame, filename, lineno, *_ = inspect.stack()[3]
    module = inspect.getmodule(frame)
    logger = logging.getLogger()
    record = logger.makeRecord(
        module.__name__,
        level,
        fn=filename,
        lno=lineno,
        msg=message,
        args=args,
        exc_info=None,
        extra=kwargs,
        sinfo=None,
    )
    logger.handle(record)

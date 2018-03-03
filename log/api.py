import inspect
import logging

DEFAULT_LEVEL = logging.INFO
DEFAULT_FORMAT = "%(levelname)s: %(name)s: %(message)s"


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

_initialized = False


def init(**kwargs):
    custom_format = kwargs.get('format')
    kwargs['level'] = kwargs.get('level', DEFAULT_LEVEL)
    kwargs['format'] = kwargs.get('format', DEFAULT_FORMAT)
    logging.basicConfig(**kwargs)
    if custom_format:
        formatter = logging.Formatter(custom_format)
        for handler in logging.root.handlers:
            handler.setFormatter(formatter)

    global _initialized
    _initialized = True


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
    if not _initialized:
        init()

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

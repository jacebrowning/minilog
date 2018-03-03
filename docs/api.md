This package is a drop-in replacement for `logging.getLogger()` objects.

It supports standard the logging API:

- `log.debug(message, *args)`
- `log.info(message, *args)`
- `log.warning(message, *args)`
- `log.error(message, *args)`
- `log.critical(message, *args)`

As well as convinience methods:

- `log.warn(message, *args)` an alias for `.warning()`

And programmatic logging:

- `log.log(level, message, *args)`

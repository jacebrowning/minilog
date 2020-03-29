# API

This package intends to be a drop-in replacement for `logging.Logger` objects. It supports the standard logging API:

```python
import log

log.debug(message, *args)
log.info(message, *args)
log.warning(message, *args)
log.error(message, *args)
log.critical(message, *args)

log.exception(message, *args)

log.log(level, message, *args)
```

As well as convenience methods:

```python
import log

log.warn(message, *args)  # warning

log.d(message, *args)     # debug
log.i(message, *args)     # info
log.w(message, *args)     # warning
log.e(message, *args)     # error

log.exc(message, *args)   # exception
```

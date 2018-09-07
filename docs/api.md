# Logging

This package intends to be a drop-in replacement for `logging.Logger` objects. It supports the standard logging API:

```python
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
log.warn(message, *args)  # warning

log.d(message, *args)     # debug
log.i(message, *args)     # info
log.w(message, *args)     # warning
log.e(message, *args)     # error

log.exc(message, *args)   # exception
```

# Configuration

Set the format for all logging handlers:

```python
log.init(format="%(levelname)s: %(name)s: %(message)s")

```

Set the level for the root logging handler:

```python
log.init(format=<…>, debug=True)
log.init(format=<…>, level=log.WARNING)
```

Replace all existing loggers before initialization:

```python
log.init(reset=True, format=<…>, level=<…>)
```

Set the logging level for specific named loggers:

```python
log.silence('selenium')
log.silence('werkzeug', 'requests', allow_warning=True)
```

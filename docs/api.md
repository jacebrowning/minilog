# Logging

The package intends to be a drop-in replacement for `logging.Logger` objects.

It supports standard the logging API:

```python
log.debug(message, *args)
log.info(message, *args)
log.warning(message, *args)
log.error(message, *args)
log.critical(message, *args)
```

As well as convenience methods:

```python
log.warn(message, *args)  # WARNING

log.d(message, *args)     # DEBUG
log.i(message, *args)     # INFO
log.w(message, *args)     # WARNING
log.e(message, *args)     # ERROR
```

And programmatic logging:

```python
log.log(level, message, *args)
```

# Configuration

Set the format for all logging handlers:

```python
log.init(format="%(levelname)s: %(name)s: %(message)s")
log.init(format="%(levelname)s: %(name)s: %(message)s", debug=True)
```

Set the logging level for specific named loggers:

```python
log.silence('selenium')
log.silence('werkzeug', 'requests', allow_warning=True)
```

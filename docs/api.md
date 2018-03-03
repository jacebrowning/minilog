This package is a drop-in replacement for `logging.Logger` objects.

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
log.warn(message, *args)  # an alias for `warning(...)`
```

And programmatic logging:

```python
log.log(level, message, *args)
```

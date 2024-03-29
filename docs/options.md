# Initialization

`minilog` defaults to INFO level using a simple log format. It supports the same initialization arguments as [`logging.basicConfig`](https://docs.python.org/3/library/logging.html#logging.basicConfig).

To set the format for all logging handlers:

```python
log.init(format="%(levelname)s: %(name)s: %(message)s")
```

To set the level for the root logging handler:

```python
log.init(format=…, level=log.WARNING)
```

### Debug Option

To simply enable debug-level logging, a convenience option is provided:

```python
log.init(format=…, debug=True)
```

### Verbosity Option

To work with frameworks that provide a `verbosity` level in their CLI frameworks (such as [Django](https://docs.djangoproject.com/en/4.0/ref/django-admin/#cmdoption-verbosity)), that can be used instead:

```python
log.init(format=…, verbosity=verbosity)
```

| Verbosity | Level       |
|-----------|-------------|
| `0`       | **ERROR**   |
| `1`       | **WARNING** |
| `2`       | **INFO**    |
| `3`       | **DEBUG**   |

### Silencing Loggers

To hide logging for specific named loggers:

```python
log.silence('selenium')
log.silence('werkzeug', 'requests', allow_warning=True)
```

### Reset Loggers

Finally, if another package has already set the logging format or level, that can be reset so that `minilog` takes over:

```python
log.reset()
log.init(…)
```

# Records

In addition to the standard [`LogRecord`](https://docs.python.org/3/library/logging.html#logrecord-attributes) attributes, the following additional patterns are available:

| Logging Format | Description                                                                                                   |
|----------------|---------------------------------------------------------------------------------------------------------------|
| `%(relpath)s`  | Full pathname of the source file where the logging call was issued relative to the current working directory. |

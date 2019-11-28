# Overview

`minilog` is a simplified wrapper for Python's standard library logging.

# Installation

Install this library directly into an activated virtual environment:

```text
$ pip install minilog
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add minilog
```

## Quick Start

Wherever you would normally construct a logger object for a module:

```python
import logging 


log = logging.getLogger(__name__)


def greet(name):
    log.info("Hello, %s!", name)
```

simply call this library directly:

```python
import log


def greet(name):
    log.info("Hello, %s!", name)
```



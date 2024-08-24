# minilog

A minimalistic logging wrapper for Python.

[![Linux Build](https://img.shields.io/github/actions/workflow/status/jacebrowning/minilog/main.yml?branch=main&label=linux)](https://github.com/jacebrowning/minilog/actions)
[![Windows Build](https://img.shields.io/appveyor/ci/jacebrowning/minilog/main.svg?label=windows)](https://ci.appveyor.com/project/jacebrowning/minilog)
[![Code Coverage](https://img.shields.io/codecov/c/github/jacebrowning/minilog)](https://codecov.io/gh/jacebrowning/minilog)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/jacebrowning/minilog.svg)](https://scrutinizer-ci.com/g/jacebrowning/minilog)
[![PyPI License](https://img.shields.io/pypi/l/minilog.svg)](https://pypi.org/project/minilog)
[![PyPI Version](https://img.shields.io/pypi/v/minilog.svg)](https://pypi.org/project/minilog)
[![PyPI Downloads](https://img.shields.io/pypi/dm/minilog.svg?color=orange)](https://pypistats.org/packages/minilog)

## Usage

Every project should utilize logging, but for simple use cases, this requires a bit too much boilerplate. Instead of including all of this in your modules:

```python
import logging

log = logging.getLogger(__name__)

def greet(name):
    log.info("Hello, %s!", name)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(name)s: %(message)s",
    )
```

with this package you can simply:

```python
import log

def greet(name):
    log.info("Hello, %s!", name)

if __name__ == "__main__":
    log.init()
```

It will produce the exact same standard library `logging` records behind the scenes with automatic formatting for non-strings.

## Installation

Install this library directly into an activated virtual environment:

```text
$ pip install minilog
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add minilog
```

## Documentation

To view additional options, please consult the [full documentation](https://minilog.readthedocs.io/en/latest/logging/).

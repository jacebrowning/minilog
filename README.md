Unix: [![Unix Build Status](https://img.shields.io/travis/jacebrowning/minilog/develop.svg)](https://travis-ci.org/jacebrowning/minilog) Windows: [![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/minilog/develop.svg)](https://ci.appveyor.com/project/jacebrowning/minilog)<br>Metrics: [![Coverage Status](https://img.shields.io/coveralls/jacebrowning/minilog/develop.svg)](https://coveralls.io/r/jacebrowning/minilog) [![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/jacebrowning/minilog.svg)](https://scrutinizer-ci.com/g/jacebrowning/minilog/?branch=develop)<br>Usage: [![PyPI Version](https://img.shields.io/pypi/v/minilog.svg)](https://pypi.python.org/pypi/minilog)

# Overview

Instead of including this boilerplate in every module:

```python
import logging

log = logging.getLogger(__name__)

def foobar(name):
    log.info("Hello, %s!", name)
```

with this package you can simply:

```python
import log

def foobar(name):
    log.info("Hello, %s!", name)
```

It will produce the exact same standard library `logging` records behind the scenes.

# Installation

```sh
$ pip install minilog
```

# Setup

Currently, `minilog` works out of the box, but that might change.



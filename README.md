[![Unix Build Status](https://img.shields.io/travis/jacebrowning/minilog/develop.svg?label=unix)](https://travis-ci.org/jacebrowning/minilog)
[![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/minilog/develop.svg?label=windows)](https://ci.appveyor.com/project/jacebrowning/minilog)
<br>
[![Coverage Status](https://img.shields.io/coveralls/jacebrowning/minilog/develop.svg)](https://coveralls.io/r/jacebrowning/minilog)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/jacebrowning/minilog.svg)](https://scrutinizer-ci.com/g/jacebrowning/minilog/?branch=develop)
<br>
[![PyPI Version](https://img.shields.io/pypi/v/minilog.svg)](https://pypi.org/project/minilog)
[![PyPI License](https://img.shields.io/pypi/l/minilog.svg)](https://pypi.org/project/minilog) 

# Overview

Every project should utilize logging, but for simple use cases, this requires a bit too much boilerplate. Instead of including all of this in your modules:

```python
import logging 

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(name)s: %(message)s",
)

log = logging.getLogger(__name__)

def greet(name):
    log.info("Hello, %s!", name)
```

with this package you can simply:

```python
import log

def greet(name):
    log.info("Hello, %s!", name)
```

It will produce the exact same standard library `logging` records behind the scenes.

# Installation

```sh
$ pip install minilog
```

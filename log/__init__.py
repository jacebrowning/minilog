from logging import DEBUG, INFO, WARNING, ERROR

from .logger import *  # pylint: disable=wildcard-import
from .helpers import init, silence

WARN = WARNING

d = debug
i = info
w = warn = warning
e = error
c = critical
exc = exception

__project__ = 'minilog'
__version__ = '0.4b2'

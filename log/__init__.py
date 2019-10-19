from logging import DEBUG, ERROR, INFO, WARNING

from .helpers import init, install_additional_formats, silence
from .logger import *  # pylint: disable=wildcard-import

WARN = WARNING

d = debug
i = info
w = warn = warning
e = error
c = critical
exc = exception

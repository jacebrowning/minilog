import logging
import os
import sys


class RelpathFormatFilter(logging.Filter):
    """Adds '%(relpath)s' as a 'LogRecord' attribute."""

    def filter(self, record):
        pathname = record.pathname
        record.relpath = None
        abs_sys_paths = [os.path.abspath(p) for p in sys.path]
        for path in sorted(abs_sys_paths, key=len, reverse=True):
            if not path.endswith(os.sep):
                path += os.sep
            if pathname.startswith(path):
                record.relpath = os.path.relpath(pathname, path)
                break
        return True


relpath_format_filter = RelpathFormatFilter()


def install(logger):
    for handler in logger.handlers:
        handler.addFilter(relpath_format_filter)

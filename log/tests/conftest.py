"""Unit tests configuration file."""

import logging


def pytest_configure(config):
    """Disable verbose output when running tests."""
    logging.basicConfig(level=logging.DEBUG)

    terminal = config.pluginmanager.getplugin('terminal')
    terminal.TerminalReporter.showfspath = False

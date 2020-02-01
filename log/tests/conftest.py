"""Unit tests configuration file."""

import logging

import pytest

import log


def pytest_configure(config):
    """Disable verbose output when running tests."""
    logging.basicConfig(level=logging.DEBUG)

    terminal = config.pluginmanager.getplugin('terminal')
    terminal.TerminalReporter.showfspath = False


@pytest.fixture(autouse=True)
def reset_state():
    log.state.default_level = None  # type: ignore

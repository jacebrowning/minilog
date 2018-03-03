# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import pytest

import log

from . import demo


def describe_api():

    def it_has_custom_warn_function(expect):
        expect(log.warn) == log.warning


def describe_output():

    def it_includes_the_caller_location(expect, caplog):
        demo.greet("caller")
        expect(caplog.text) == \
            "demo.py                      5 ERROR    Hello, caller!\n"

    @pytest.mark.last
    def it_can_be_formatted_with_init(expect, caplog):
        log.init(format="%(levelname)s: %(name)s: %(message)s")
        demo.greet("format")
        expect(caplog.text) == "ERROR: tests.demo: Hello, format!\n"

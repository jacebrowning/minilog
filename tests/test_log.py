# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import log

from . import demo


def describe_api():

    def it_has_custom_warn_function(expect):
        expect(log.warn) == log.warning


def describe_output():

    def it_uses_the_caller_name(expect, caplog):
        demo.foobar()
        expect(caplog.text) == "ERROR: tests.demo: Hello, world!\n"

# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import pytest

import log

from . import demo, other


def describe_text():

    def it_includes_the_caller_location(expect, caplog):
        demo.greet("caller")
        expect(caplog.text) == \
            "demo.py                      5 ERROR    Hello, caller!\n"

    @pytest.mark.last
    def it_can_be_formatted_with_init(expect, caplog):
        log.init(format=log.helpers.DEFAULT_FORMAT, level=log.WARNING)
        demo.greet("format")
        expect(caplog.text) == "ERROR: tests.demo: Hello, format!\n"


def describe_silence():

    def when_off(expect, caplog):
        log.silence('3rd-party')
        other.do_3rd_party_thing()
        expect(caplog.records) == []

    def with_errors(expect, caplog):
        log.silence('3rd-party', allow_error=True)
        other.do_3rd_party_thing()
        expect(len(caplog.records)) == 1

    def with_warnings(expect, caplog):
        log.silence('3rd-party', allow_warning=True)
        other.do_3rd_party_thing()
        expect(len(caplog.records)) == 2

    def with_infos(expect, caplog):
        log.silence('3rd-party', allow_info=True)
        other.do_3rd_party_thing()
        expect(len(caplog.records)) == 3

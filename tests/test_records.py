# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import os

import pytest
from freezegun import freeze_time

import log

from . import demo, other


def describe_text():
    def it_includes_the_caller_location(expect, caplog):
        demo.greet("caller")

        expect(caplog.text) == "ERROR    tests.demo:demo.py:5 Hello, caller!\n"

    @pytest.mark.last
    @freeze_time('2019-01-15')
    def it_can_be_formatted_with_init(expect, caplog):
        log.init(
            level=log.WARNING,
            format='%(asctime)s %(relpath)s:%(lineno)s: %(message)s',
            datefmt='%Y-%m',
        )

        demo.greet("format")

        if os.name == 'nt':
            expect(caplog.text) == "2019-01 tests\\demo.py:5: Hello, format!\n"
        else:
            expect(caplog.text) == "2019-01 tests/demo.py:5: Hello, format!\n"

    def it_can_include_exceptions(expect, caplog):
        try:
            print(1 / 0)
        except ZeroDivisionError:
            log.exception("exception")

        expect(caplog.text).contains('Traceback ')
        expect(caplog.text).contains('test_records.py", line 37, ')
        expect(caplog.text).contains('ZeroDivisionError')


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

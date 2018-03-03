# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import logging

import pytest

from log import api


def describe_log():

    def it_sets_level_and_message(expect, caplog):
        api.log(logging.DEBUG, "foobar")
        expect(caplog.records[-1].levelname) == 'DEBUG'
        expect(caplog.records[-1].message) == "foobar"


@pytest.mark.parametrize("name, levelname", [
    ('critical', 'CRITICAL'),
    ('debug', 'DEBUG'),
    ('error', 'ERROR'),
    # ('exception', 'ERROR'),
    ('info', 'INFO'),
    ('warn', 'WARNING'),
    ('warning', 'WARNING'),
])
def test_level_mapping(expect, caplog, name, levelname):
    getattr(api, name)("message")
    expect(caplog.records[-1].levelname) == levelname

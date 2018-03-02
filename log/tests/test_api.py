# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import logging

from log import api


def describe_log():

    def it_sets_level_and_message(expect, caplog):
        api.log(logging.ERROR, "foobar")
        expect(caplog.records[-1].levelname) == 'ERROR'
        expect(caplog.records[-1].message) == "foobar"

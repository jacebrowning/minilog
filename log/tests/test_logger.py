# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import logging

from log import logger


def describe_log():
    def it_sets_level_and_message(expect, caplog):
        logger.log(logging.DEBUG, "foobar")
        expect(caplog.records[-1].levelname) == 'DEBUG'
        expect(caplog.records[-1].message) == "foobar"

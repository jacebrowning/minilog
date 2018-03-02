# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import log


def describe_api():

    def it_has_custom_warn_function(expect):
        expect(log.warn) == log.warning

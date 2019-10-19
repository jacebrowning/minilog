# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import logging

from log import state, utils


def describe_create_logger_record():

    def it_uses_the_default_log_level_for_new_loggers(expect):
        state.default_level = logging.INFO

        expect(utils.create_logger_record(
            logging.DEBUG, 'hello', module_name='my_new_module'
        )) == False

        expect(utils.create_logger_record(
            logging.INFO, 'hello', module_name='my_new_module'
        )) == True

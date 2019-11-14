# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import logging

from log import state, utils


def describe_create_logger_record():

    def it_uses_the_default_log_level_for_new_loggers(expect):
        state.default_level = logging.INFO

        expect(utils.create_logger_record(
            logging.DEBUG, 'hello', module_name='new_module'
        )) == False

        expect(utils.create_logger_record(
            logging.INFO, 'hello', module_name='new_module'
        )) == True

        expect(utils.create_logger_record(
            logging.WARNING, 'hello', module_name='new_module'
        )) == True

    def it_inherits_the_parent_logging_level(expect):
        state.default_level = logging.INFO

        logger = logging.getLogger('parent_module')
        logger.level = logging.WARNING

        expect(utils.create_logger_record(
            logging.DEBUG, 'hello', module_name='parent_module.new_module'
        )) == False

        expect(utils.create_logger_record(
            logging.INFO, 'hello', module_name='parent_module.new_module'
        )) == False

        expect(utils.create_logger_record(
            logging.WARNING, 'hello', module_name='parent_module.new_module'
        )) == True

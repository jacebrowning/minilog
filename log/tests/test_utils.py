# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import logging

from log.utils import create_logger_record, parse_name


def describe_create_logger_record():
    def it_uses_the_default_log_level_for_new_loggers(expect, monkeypatch):
        monkeypatch.setattr(logging.root, 'level', logging.INFO)

        expect(create_logger_record(logging.DEBUG, 'hello', name='new')) == False
        expect(create_logger_record(logging.INFO, 'hello', name='new')) == True
        expect(create_logger_record(logging.WARNING, 'hello', name='new')) == True

    def it_inherits_the_parent_logging_level(expect):
        logger = logging.getLogger('root')
        logger.level = logging.WARNING

        expect(create_logger_record(logging.DEBUG, 'hello', name='root.new')) == False
        expect(create_logger_record(logging.INFO, 'hello', name='root.new')) == False
        expect(create_logger_record(logging.WARNING, 'hello', name='root.new')) == True


def describe_parse_name():
    def it_uses_the_filename_when_main(expect):
        frame_info = {'__file__': 'my_package/my_module.py'}
        expect(parse_name('__main__', frame_info)[0]) == 'my_package.my_module'

    def it_handles_interactive_sessions(expect):
        expect(parse_name('__main__', {})[0]) == 'interactive'

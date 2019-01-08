# pylint: disable=unused-variable,expression-not-assigned

from unittest.mock import call, patch

from log import helpers


def describe_init():
    @patch('logging.basicConfig')
    def with_verbosity_0(config, expect):
        helpers.init(format='%(message)s', verbosity=0)
        expect(config.mock_calls) == [call(format='%(message)s', level=40)]

    @patch('logging.basicConfig')
    def with_verbosity_1(config, expect):
        helpers.init(format='%(message)s', verbosity=1)
        expect(config.mock_calls) == [call(format='%(message)s', level=30)]

    @patch('logging.basicConfig')
    def with_verbosity_2(config, expect):
        helpers.init(format='%(message)s', verbosity=2)
        expect(config.mock_calls) == [call(format='%(message)s', level=20)]

    @patch('logging.basicConfig')
    def with_verbosity_3(config, expect):
        helpers.init(format='%(message)s', verbosity=3)
        expect(config.mock_calls) == [call(format='%(message)s', level=10)]

    @patch('logging.basicConfig')
    def with_verbosity_0_and_debug(config, expect):
        helpers.init(format='%(message)s', verbosity=0, debug=True)
        expect(config.mock_calls) == [call(format='%(message)s', level=10)]

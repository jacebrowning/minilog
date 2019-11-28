# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

import pytest

import log


@pytest.mark.parametrize(
    'name, levelname',
    [
        ('c', 'CRITICAL'),
        ('critical', 'CRITICAL'),
        ('d', 'DEBUG'),
        ('debug', 'DEBUG'),
        ('e', 'ERROR'),
        ('error', 'ERROR'),
        ('exc', 'ERROR'),
        ('exception', 'ERROR'),
        ('i', 'INFO'),
        ('info', 'INFO'),
        ('w', 'WARNING'),
        ('warn', 'WARNING'),
        ('warning', 'WARNING'),
    ],
)
def test_level_mapping(expect, caplog, name, levelname):
    getattr(log, name)("message")
    expect(caplog.records[-1].levelname) == levelname
